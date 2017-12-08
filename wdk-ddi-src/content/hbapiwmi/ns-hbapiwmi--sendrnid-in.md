---
UID: NS.hbapiwmi._SendRNID_IN
title: SendRNID_IN
author: windows-driver-content
description: The SendRNID_IN structure is used to deliver input parameter data to the SendRNID WMI method.
old-location: storage\sendrnid_in.htm
old-project: storage
ms.assetid: 668c4d1a-52e8-49ea-bd19-e789dfa8dfa5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SendRNID_IN, SendRNID_IN, *PSendRNID_IN
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
req.alt-api: SendRNID_IN
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

# SendRNID_IN structure



## -description
<p>The SendRNID_IN structure is used to deliver input parameter data to the <a href="storage.sendrnid">SendRNID</a> WMI method.</p>


## -syntax

````
typedef struct _SendRNID_IN {
  UCHAR wwn[8];
  ULONG wwntype;
} SendRNID_IN, *PSendRNID_IN;
````


## -struct-fields
<dl>

### -field wwn

<dd>
<p>Contains a worldwide name for the port to which the request node identification data (RNID) command is sent. </p>
</dd>

### -field wwntype

<dd>
<p>Deprecated. Do not use. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SendRNID_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbaadaptermethods_wmi_class">MSFC_HBAAdapterMethods WMI Class</a>.</p>

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
<a href="storage.sendrnid">SendRNID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SendRNID_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
