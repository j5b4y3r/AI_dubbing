import numpy as np
def assign_speakers_to_transcript(transcript_segments, speaker_labels, frame_times):
    updated_segments = []

    # Iterate over transcript segments and assign the corresponding speaker label
    for i, segment in enumerate(transcript_segments):
        if isinstance(segment, dict):
            try:
                # Convert 'start' and 'end' times to integers (if necessary)
                start_time = int(segment['start'])
                end_time = int(segment['end'])
            except (KeyError, ValueError) as e:
                print(f"Error accessing start/end times in segment {i}: {e}")
                continue
        else:
            print("segments is not dictionary")    
            break

        # Find the frame indices where the frame times fall within the current segment
        frames_in_segment = np.where((frame_times >= start_time) & (frame_times <= end_time))[0]

        if len(frames_in_segment) > 0:
            # Find the most frequent speaker label within the segment
            speaker_for_segment = np.bincount(speaker_labels[frames_in_segment]).argmax()
        else:
            speaker_for_segment = "unknown"

        # Add the speaker label to the transcript segment
        updated_segment = segment.copy()  # Create a copy to avoid modifying the original object
        updated_segment['speaker'] = speaker_for_segment
        updated_segments.append(updated_segment)

    return updated_segments
