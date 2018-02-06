---
UID: NA:wudfwdm
ms.assetid: 09d3bb45-c5d1-38ed-82eb-ef09ddbc1057
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# wudfwdm.h header



wudfwdm.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [ARGUMENT_PRESENT](nf-wudfwdm-argument_present.md) | The ARGUMENT_PRESENT macro takes an argument pointer and returns FALSE if the pointer is NULL. Otherwise, it returns TRUE. |
| [InitializeObjectAttributes](nf-wudfwdm-initializeobjectattributes.md) | The InitializeObjectAttributes macro initializes the opaque OBJECT_ATTRIBUTES structure, which specifies the properties of an object handle to routines that open handles. |



## Structures
| Title | Description |
| ---- |:---- |
| [_OBJECT_ATTRIBUTES](ns-wudfwdm-_object_attributes.md) | The OBJECT_ATTRIBUTES structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects. |
| [_UNICODE_STRING](ns-wudfwdm-_unicode_string.md) | The UNICODE_STRING structure is used to define Unicode strings. |