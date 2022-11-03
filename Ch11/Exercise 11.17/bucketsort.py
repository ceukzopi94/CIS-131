"""BucketSort Base Class"""

class BucketSort:
    """BucketSort Base Class"""

    def __init__(self):
        self.bucket = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[]]

    
    @property
    def bucket(self):
        """Return the bucket 2D list"""

    
    @bucket.setter
    def bucket(self, list):
        """Sets the bucket"""
        self._bucket = list

    
    def sort(self, list):
        """Sorts a list into a bucket."""
        