---
UID: NS.ntddchgr._CHANGER_ELEMENT
title: CHANGER_ELEMENT
author: windows-driver-content
description: The CHANGER_ELEMENT structure contains a description of a changer element.
old-location: storage\changer_element.htm
old-project: storage
ms.assetid: 85035147-0ae8-482a-9a12-1e4e53ae1969
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CHANGER_ELEMENT, CHANGER_ELEMENT, *PCHANGER_ELEMENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANGER_ELEMENT
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
req.iface: 
---

# CHANGER_ELEMENT structure



## -description
<p>The CHANGER_ELEMENT structure contains a description of a changer element. </p>


## -syntax

````
typedef struct _CHANGER_ELEMENT {
  ELEMENT_TYPE ElementType;
  ULONG        ElementAddress;
} CHANGER_ELEMENT, *PCHANGER_ELEMENT;
````


## -struct-fields
<dl>

### -field <b>ElementType</b>

<dd>
<p>Indicates the type of element. Can be one of the following values taken from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553754">ELEMENT_TYPE</a> enumeration.</p>
<p></p>
<dl>

### -field <a id="AllElements"></a><a id="allelements"></a><a id="ALLELEMENTS"></a><b>AllElements</b>

<dd>
<p>All elements of a changer, including its robotic transport, drives, slots, and IEport. <b>AllElements</b> is valid only in a <b>ChangerGetElementStatus</b> or <b>ChangerInitializeElementStatus</b> call.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerTransport"></a><a id="changertransport"></a><a id="CHANGERTRANSPORT"></a><b>ChangerTransport</b>

<dd>
<p>The changer's robotic transport element, which is used to move media between IEports, slots, and drives.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerSlot"></a><a id="changerslot"></a><a id="CHANGERSLOT"></a><b>ChangerSlot</b>

<dd>
<p>A storage element, which is a slot in the changer in which media is stored when not mounted in a drive.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerIEPort"></a><a id="changerieport"></a><a id="CHANGERIEPORT"></a><b>ChangerIEPort</b>

<dd>
<p>An import/export element (IEport), which is a single or multiple-cartridge access port in some changers. An element is an IEport only if it is possible to move a piece of media from a slot to the IEport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerDrive"></a><a id="changerdrive"></a><a id="CHANGERDRIVE"></a><b>ChangerDrive</b>

<dd>
<p>A data transfer element where data can be read from and written to media. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerDoor"></a><a id="changerdoor"></a><a id="CHANGERDOOR"></a><b>ChangerDoor</b>

<dd>
<p>A mechanism that provides access to all media in a changer at one time (as compared to an IEport that provides access to one or more, but not all, media). For example, a large front door or a magazine that contains all media in the changer are elements of this type. <b>ChangerDoor</b> is valid only in a <b>ChangerSetAccess</b> call.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="ChangerKeypad"></a><a id="changerkeypad"></a><a id="CHANGERKEYPAD"></a><b>ChangerKeypad</b>

<dd>
<p>The keypad or other input control on the front panel of a changer. <b>ChangerKeypad</b> is valid only in a <b>ChangerSetAccess</b> call.</p>
</dd>
</dl>
</dd>

### -field <b>ElementAddress</b>

<dd>
<p>Indicates the element's zero-based address used by the system. A changer miniclass driver is responsible for translating this address to the device-specific address used by the changer.</p>
</dd>
</dl>

## -remarks
<p>CHANGER_ELEMENT is used by both the changer class driver and a changer miniclass driver to describe a changer element. </p>

<p>On input, a changer miniclass driver must translate the zero-based address in <b>ElementAddress</b> to a device-specific address before accessing the element. On output, the driver must translate a device-specific address to the zero-based equivalent before filling in <b>ElementAddress</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551459">CHANGER_ELEMENT_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551461">CHANGER_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553754">ELEMENT_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_ELEMENT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
