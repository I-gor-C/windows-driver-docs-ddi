---
UID: NE.ntddchgr._ELEMENT_TYPE
title: _ELEMENT_TYPE
author: windows-driver-content
description: The ELEMENT_TYPE enumeration provides a list of changer element types defined by the SCSI-3 specification.
old-location: storage\element_type.htm
old-project: storage
ms.assetid: 909e0645-3824-40ff-bec9-128a9939eb1e
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _ELEMENT_TYPE, PELEMENT_TYPE, ELEMENT_TYPE, *PELEMENT_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ELEMENT_TYPE
req.alt-loc: ntddchgr.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# _ELEMENT_TYPE enumeration



## -description
The ELEMENT_TYPE enumeration provides a list of changer element types defined by the <i>SCSI-3</i> specification. 



## -syntax

````
typedef enum _ELEMENT_TYPE { 
  AllElements        = 0,
  ChangerTransport   = 1,
  ChangerSlot        = 2,
  ChangerIEPort      = 3,
  ChangerDrive       = 4,
  ChangerDoor        = 5,
  ChangerKeypad      = 6,
  ChangerMaxElement  = 7
} ELEMENT_TYPE, *PELEMENT_TYPE;
````


## -enum-fields

### -field AllElements

Indicates all elements of a changer, including its robotic transport, drives, slots, and IEport. <b>AllElements</b> is valid only in a <a href="storage.changergetelementstatus">ChangerGetElementStatus</a> or <a href="storage.changerinitializeelementstatus">ChangerInitializeElementStatus</a> call.


### -field ChangerTransport

Indicates the changer's robotic transport element, which is used to move media between IEports, slots, and drives.


### -field ChangerSlot

Indicates a storage element, which is a slot in the changer in which media is stored when not mounted in a drive.


### -field ChangerIEPort

Indicates an import/export element (IEport), which is a single or multiple-cartridge access port in some changers. An element is an IEport only if it is possible to move a piece of media from a slot to the IEport.


### -field ChangerDrive

Indicates a data transfer element where data can be read from and written to media. 


### -field ChangerDoor

Indicates a mechanism that provides access to all media in a changer at one time (as compared to an IEport that provides access to one or more, but not all, media). For example, a large front door or a magazine that contains all media in the changer are elements of this type. <b>ChangerDoor</b> is valid only in a <a href="storage.changersetaccess">ChangerSetAccess</a> call.


### -field ChangerKeypad

Indicates the keypad or other input control on the front panel of a changer. <b>ChangerKeypad</b> is valid only in a <a href="storage.changersetaccess">ChangerSetAccess</a> call.


### -field ChangerMaxElement

Indicates the upper limit of the enumerators in this enumeration. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.changergetelementstatus">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="storage.changerinitializeelementstatus">ChangerInitializeElementStatus</a>
</dt>
<dt>
<a href="storage.changersetaccess">ChangerSetAccess</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ELEMENT_TYPE enumeration%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

