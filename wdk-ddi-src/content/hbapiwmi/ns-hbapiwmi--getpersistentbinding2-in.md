---
UID: NS.hbapiwmi._GetPersistentBinding2_IN
title: GetPersistentBinding2_IN
author: windows-driver-content
description: The GetPersistentBinding2_IN structure is used to deliver input parameter data to the GetPersistentBinding2 WMI method.
old-location: storage\getpersistentbinding2_in.htm
old-project: storage
ms.assetid: 646378f8-9037-4c40-bcbc-5ffe380e6279
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetPersistentBinding2_IN, GetPersistentBinding2_IN, *PGetPersistentBinding2_IN
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
req.alt-api: GetPersistentBinding2_IN
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

# GetPersistentBinding2_IN structure



## -description
<p>The GetPersistentBinding2_IN structure is used to deliver input parameter data to the <a href="storage.getpersistentbinding2">GetPersistentBinding2</a> WMI method.</p>


## -syntax

````
typedef struct _GetPersistentBinding2_IN {
  UCHAR PortWWN[8];
  ULONG InEntryCount;
} GetPersistentBinding2_IN, *PGetPersistentBinding2_IN;
````


## -struct-fields
<dl>

### -field PortWWN

<dd>
<p>Contains a worldwide name that indicates the port whose persistent bindings are to be retrieved. </p>
</dd>

### -field InEntryCount

<dd>
<p>Indicates the number of binding entries that the WMI provider can report.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetPersistentBinding2_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>.</p>

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
<a href="storage.getpersistentbinding2">GetPersistentBinding2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetPersistentBinding2_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
