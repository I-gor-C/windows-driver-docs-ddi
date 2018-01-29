---
UID : NA:engextcpp
ms.assetid : 4849a6b1-830f-3826-8f7f-f7451944fa5f
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# engextcpp.h header



engextcpp.h contains the following programming interfaces:


## Classes
| Title | Description |
| ---- |:---- |
| [ExtRemoteData](nl-engextcpp-extremotedata.md) | The ExtRemoteData class provides a wrapper around a small section of a target's memory. ExtRemoteData automatically retrieves the memory and provides a number of convenience methods. |
| [ExtRemoteTypedList](nl-engextcpp-extremotetypedlist.md) | The ExtRemoteTypedList class extends the ExtRemoteList class. The ExtRemoteTypedList class adds type information allowing each item in the list to be represented by an instance of the ExtRemoteTyped class. |




## Functions
| Title | Description |
| ---- |:---- |
| [EXT_COMMAND](nf-engextcpp-ext_command.md) | The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows: |
| [EXT_COMMAND_METHOD](nf-engextcpp-ext_command_method.md) | The EXT_COMMAND_METHOD macro declares an extension command from inside the definition of the EXT_CLASS class. |



## Structures
| Title | Description |
| ---- |:---- |
| [ExtKnownStruct](ns-engextcpp-extknownstruct.md) | The ExtKnownStruct structure is used to specify how a target's structure can be formatted for output. |