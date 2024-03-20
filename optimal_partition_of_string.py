class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 0

        for char in s:
            if char in seen:
                # We've seen this character before, so we start a new partition.
                partitions += 1
                seen.clear()  # Reset the seen characters for the new partition.
            
            seen.add(char)
        
        # Don't forget to count the partition we are on when the string ends
        partitions += 1 if seen else 0

        return partitions
