---
UID: NS.hbapiwmi._GetFcpPersistentBinding_IN
title: GetFcpPersistentBinding_IN
author: windows-driver-content
description: The GetFcpPersistentBinding_IN structure is used to pass input parameter data to the GetFcpPersistentBinding WMI method
old-location: storage\getfcppersistentbinding_in.htm
old-project: storage
ms.assetid: b08354c8-ef4e-4330-8a3b-dcfe3a722a5d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetFcpPersistentBinding_IN, GetFcpPersistentBinding_IN, *PGetFcpPersistentBinding_IN
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
req.alt-api: GetFcpPersistentBinding_IN
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

# GetFcpPersistentBinding_IN structure



## -description
<p>The GetFcpPersistentBinding_IN structure is used to pass input parameter data to the <a href="storage.getfcppersistentbinding">GetFcpPersistentBinding</a> WMI method </p>


## -syntax

````
typedef struct _GetFcpPersistentBinding_IN {
  ULONG InEntryCount;
} GetFcpPersistentBinding_IN, *PGetFcpPersistentBinding_IN;
````


## -struct-fields
<dl>

### -field InEntryCount

<dd>
<p>Indicates the number of binding entries that will fit in the buffer that the WMI client provides when it calls the <a href="storage.getfcppersistentbinding">GetFcpPersistentBinding</a> WMI method.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetFcpPersistentBinding_IN structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>.</p>

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
<a href="storage.getfcppersistentbinding">GetFcpPersistentBinding</a>
</dt>
<dt>
<a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetFcpPersistentBinding_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
