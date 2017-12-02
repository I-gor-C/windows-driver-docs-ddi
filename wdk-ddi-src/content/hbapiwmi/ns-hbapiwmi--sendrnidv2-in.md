---
UID: NS.hbapiwmi._SendRNIDV2_IN
title: SendRNIDV2_IN
author: windows-driver-content
description: The SendRNIDV2_IN structure is used to deliver input parameter data to the SendRNIDV2 WMI method.
old-location: storage\sendrnidv2_in.htm
old-project: storage
ms.assetid: b9c0833d-96ac-41cb-815f-b2df27f46cb4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SendRNIDV2_IN, SendRNIDV2_IN, *PSendRNIDV2_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SendRNIDV2_IN
req.alt-loc: hbapiwmi.h
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

# SendRNIDV2_IN structure



## -description
<p>The SendRNIDV2_IN structure is used to deliver input parameter data to the <a href="storage.sendrnidv2">SendRNIDV2</a> WMI method.</p>


## -syntax

````
typedef struct _SendRNIDV2_IN {
  UCHAR PortWWN[8];
  UCHAR DestWWN[8];
  ULONG DestFCID;
  ULONG NodeIdDataFormat;
} SendRNIDV2_IN, *PSendRNIDV2_IN;
````


## -struct-fields
<dl>

### -field PortWWN

<dd>
<p>Contains a worldwide name for the local port through which the version 2 request node identification data (RNIDV2) command is sent. </p>
</dd>

### -field DestWWN

<dd>
<p>Contains a worldwide name for the destination port. </p>
</dd>

### -field DestFCID

<dd>
<p>Contains an address identifier of the destination port. For a description of the values that this member can have, see the T11 committee's specification for <i>Fibre Channel HBA API</i>.</p>
</dd>

### -field NodeIdDataFormat

<dd>
<p>Indicates the node identification data format. For a description of the values that this member can have, see the T11 committee's specification for <i>Fibre Channel HBA API</i>. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SendRNIDV2_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.sendrnidv2">SendRNIDV2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SendRNIDV2_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
