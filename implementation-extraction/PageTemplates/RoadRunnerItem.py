class RoadRunnerItems():
    # RoadRunnerItems is list of RoadRunnerItem
    def __init__(self, RoadRunnerItems):
        self.RoadRunnerItems = RoadRunnerItems

    class RoadRunnerItem():
        def __init__(self, scoreDiff, scoreMain, blockFeature, file1, file2):
            self.ScoreDiff = scoreDiff
            self.ScoreMain = scoreMain
            self.BlockFeature = blockFeature
            self.File1 = file1
            self.File2 = file2
