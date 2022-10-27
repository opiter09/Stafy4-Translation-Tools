import ndspy.bmg

bmg = ndspy.bmg.BMG.fromFile("0009_textFiles/582164_585268.BMG")

out = ndspy.bmg.BMG.fromMessages(bmg.messages + [ bmg.messages[2] ])
out.endianness = ">"
out.encoding = "shift-jis"
out.saveToFile("0009_textFiles/NEW_582164_585268.BMG")