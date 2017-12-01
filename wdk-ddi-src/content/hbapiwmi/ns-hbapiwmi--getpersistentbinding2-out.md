---
UID: NS.hbapiwmi._GetPersistentBinding2_OUT
title: GetPersistentBinding2_OUT
author: windows-driver-content
description: The GetBindingSupport_OUT structure is used to report the output parameter data of the GetPersistentBinding2 WMI method to the WMI client.
old-location: storage\getpersistentbinding2_out.htm
old-project: storage
ms.assetid: 883a7a56-ecb9-428f-a15a-ba428a626bed
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetPersistentBinding2_OUT, GetPersistentBinding2_OUT, *PGetPersistentBinding2_OUT
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
req.alt-api: GetPersistentBinding2_OUT
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

# GetPersistentBinding2_OUT structure



## -description
<p>The GetBindingSupport_OUT structure is used to report the output parameter data of the <a href="storage.getpersistentbinding2">GetPersistentBinding2</a> WMI method to the WMI client.</p>


## -syntax

````
typedef struct _GetPersistentBinding2_OUT {
  ULONG               HBAStatus;
  ULONG               TotalEntryCount;
  ULONG               OutEntryCount;
  HBAFCPBindingEntry2 Bindings[1];
} GetPersistentBinding2_OUT, *PGetPersistentBinding2_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>. </p>
</dd>

### -field <b>TotalEntryCount</b>

<dd>
<p>Indicates the number of binding entries that the WMI provider can report.</p>
</dd>

### -field <b>OutEntryCount</b>

<dd>
<p>Indicates the total number of persistent bindings retrieved by the GetPersistentBinding2 method.</p>
</dd>

### -field <b>Bindings</b>

<dd>
<p>Contains an array of structures of type <a href="..\hbapiwmi\ns-hbapiwmi--hbafcpbindingentry2.md">HBAFCPBindingEntry2</a> that describe an HBA's bindings between operating system and fibre channel protocol (FCP) identifiers.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the GetPersistentBinding2_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetPersistentBinding2_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
