class AutomaticItems():
    # AutomaticItems is list of RoadRunnerItem
    def __init__(self, AutomaticItems):
        self.AutomaticItems = AutomaticItems

    class AutomaticItem():
        def __init__(self, scoreDiff, scoreMain, blockFeature, file1, file2):
            self.ScoreDiff = scoreDiff
            self.ScoreMain = scoreMain
            self.BlockFeature = blockFeature
            self.File1 = file1
            self.File2 = file2
