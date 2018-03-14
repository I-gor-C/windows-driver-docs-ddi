---
UID: NA:engextcpp
ms.assetid: 4849a6b1-830f-3826-8f7f-f7451944fa5f
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Engextcpp.h header



This header is used by Debugger. For more information, see
- [Debugger](../_debugger/index.md)

Engextcpp.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ExtKnownStruct structure](ns-engextcpp-extknownstruct.md) | The ExtKnownStruct structure is used to specify how a target's structure can be formatted for output. |

## Classes

| Title   | Description   |
| ---- |:---- |
| [ExtExtension class](nl-engextcpp-extextension~r1.md) | The ExtExtension class is the base class for the C++ class that represents the EngExtCpp extension library. |
| [ExtRemoteData class](nl-engextcpp-extremotedata.md) | The ExtRemoteData class provides a wrapper around a small section of a target's memory. ExtRemoteData automatically retrieves the memory and provides a number of convenience methods. |
| [ExtRemoteList class](nl-engextcpp-extremotelist.md) | The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list. |
| [ExtRemoteTyped class](nl-engextcpp-extremotetyped.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTypedList class](nl-engextcpp-extremotetypedlist.md) | The ExtRemoteTypedList class extends the ExtRemoteList class. The ExtRemoteTypedList class adds type information allowing each item in the list to be represented by an instance of the ExtRemoteTyped class. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [EXT_COMMAND macro](nf-engextcpp-ext_command.md) | The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows |
| [EXT_COMMAND_METHOD macro](nf-engextcpp-ext_command_method.md) | The EXT_COMMAND_METHOD macro declares an extension command from inside the definition of the EXT_CLASS class. |

## Methods

| Title   | Description   |
| ---- |:----

# engextcpp.h header



engextcpp.h contains the following programming interfaces:


## Classes
| Title | Description |
| ---- |:---- |
| [ExtExtension](nl-engextcpp-extextension~r1.md) | The ExtExtension class is the base class for the C++ class that represents the EngExtCpp extension library. |
| [ExtRemoteData](nl-engextcpp-extremotedata.md) | The ExtRemoteData class provides a wrapper around a small section of a target's memory. ExtRemoteData automatically retrieves the memory and provides a number of convenience methods. |
| [ExtRemoteList](nl-engextcpp-extremotelist.md) | The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list. |
| [ExtRemoteTyped](nl-engextcpp-extremotetyped.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
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