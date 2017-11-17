---
UID: NS.hbaapi.HBA_FCPBinding
title: HBA_FCPBinding
author: windows-driver-content
description: The HBA_FCPBinding structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of logical units.
old-location: storage\hba_fcpbinding.htm
ms.assetid: e06b82f7-2b48-47e8-b6fa-c86b790e8019
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_FCPBINDING
req.alt-loc: hbaapi.h
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
ms.keywords: HBA_FCPBinding, HBA_FCPBINDING, *PHBA_FCPBINDING
req.iface: 
---

# HBA_FCPBinding structure



## -description
<p>The HBA_FCPBinding structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of logical units. </p>


## -syntax

````
typedef struct HBA_FCPBinding {
  HBA_UINT32          NumberOfEntries;
  HBA_FCPBINDINGENTRY entry[1];
} HBA_FCPBINDING, *PHBA_FCPBINDING;
````


## -struct-fields
<dl>

### -field <b>NumberOfEntries</b>

<dd>
<p>Indicates the number of bindings.</p>
</dd>

### -field <b>entry</b>

<dd>
<p>Contains a variable length array of structures of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff556058">HBA_FCPBindingEntry</a> each of which defines a binding between a pair of operating system and fibre channel protocol (FCP) identifiers for a logical unit. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556058">HBA_FCPBindingEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556034">HBAFCPBindingEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBA_FCPBinding structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
