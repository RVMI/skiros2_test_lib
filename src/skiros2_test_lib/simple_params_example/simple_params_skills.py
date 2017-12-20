#################################################################################
# Software License Agreement (BSD License)
#
# Copyright (c) 2016, Francesco Rovida
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the copyright holder nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################

from skiros2_skill.core.skill import SkillDescription, SkillBase, ParallelFf
from skiros2_common.core.params import ParamTypes
from skiros2_common.core.world_element import Element
        
    
#################################################################################
# Description
#################################################################################
    
class TrajectoryCoordinator(SkillDescription):
    def createDescription(self):
        self._type = ":TrajectoryCoordinator"
        #=======Params=========
        #self.addParam("Container", Element(":Location"), ParamTypes.World)
        #self.addParam("Object", Element(":Product"), ParamTypes.Optional)
        self.addParam("Pose", Element("skiros:TransformationPose"), ParamTypes.Optional)
        self.addParam("Pose2", Element("skiros:TransformationPose"), ParamTypes.Optional)                 
        
#################################################################################
# Implementation
#################################################################################
        
class trajectory_coordinator(SkillBase):
    """
    Tree is:
    ----->:trajectory_coordinator (|Fs|)
    ------->:TrajectoryGenerator
    ------->:TrajectoryConsumer

    """
    def createDescription(self):
        self.setDescription(TrajectoryCoordinator(), self.__class__.__name__)
        
    def expand(self, skill):
        skill.setProcessor(ParallelFf())
        skill.addChild(self.getSkill(":TrajectoryGenerator", ""))
        skill.addChild(self.getSkill(":TrajectoryConsumer", ""))
        
