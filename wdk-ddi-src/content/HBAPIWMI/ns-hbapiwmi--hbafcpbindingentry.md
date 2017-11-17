---
UID: NS.hbapiwmi._HBAFCPBindingEntry
title: HBAFCPBindingEntry
author: windows-driver-content
description: The HBAFCPBindingEntry structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.
old-location: storage\hbafcpbindingentry.htm
ms.assetid: fa0f20e1-7d63-48e8-8270-8dab566f5947
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h, Hbaapi.h, Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBAFCPBindingEntry
req.alt-loc: Hbapiwmi.h
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
ms.keywords: HBAFCPBindingEntry, HBAFCPBindingEntry, *PHBAFCPBindingEntry
req.iface: 
---

# HBAFCPBindingEntry structure



## -description
<p>The HBAFCPBindingEntry structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit. </p>


## -syntax

````
typedef struct _HBAFCPBindingEntry {
  ULONG     Type;
  HBAFCPID  FCPId;
  HBAScsiID ScsiId;
} HBAFCPBindingEntry, *PHBAFCPBindingEntry;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Contains a binding type that indicates how the target is specified in the binding. This member can have any of the following values:  </p>
<table>
<tr>
<th>Type Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_D_ID</p>
</td>
<td>
<p>Indicates that the target is identified by its fibre channel protocol (FCP) ID. The <b>Fcid</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556038">HBAFCPID</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_WWPN</p>
</td>
<td>
<p>Indicates that the target is identified by its worldwide port name. The <b>PortWWN</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556038">HBAFCPID</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_WWNN</p>
</td>
<td>
<p>Indicates that the fibre channel target device is identified by its worldwide node name. The <b>NodeWWN</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556038">HBAFCPID</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_LUID</p>
</td>
<td>
<p>Indicates that the target is identified by its fibre channel logical unit ID. The <b>FcpLun</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556038">HBAFCPID</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TARGETS</p>
</td>
<td>
<p>Indicates that the system should automatically generate target mappings from logical unit numbers to fibre channel protocol identifiers. </p>
</td>
</tr>
</table>
<p> </p>
<p>You must include file <i>hbaapi.h </i>to use the symbolic constants in this table (See the <b>Headers</b> section).</p>
<p>For a comparable set of values that define how an HBA specifies targets and logical units in the persistent bindings that it maintains, see the WMI property qualifier <a href="https://msdn.microsoft.com/library/windows/hardware/ff556046">HBA_BIND_TYPE</a>. </p>
<p>For a more detailed description of the values that this member can have, see the T11 committee's <i>Fibre Channel HBA API</i> specification. </p>
</dd>

### -field <b>FCPId</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff556038">HBAFCPID</a> that contains the FCP identifier for the logical unit and information about the port to be queried for information about the device.</p>
</dd>

### -field <b>ScsiId</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff556042">HBAScsiID</a> that contains the information that uniquely identifies a logical unit for the operating system. </p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of this structure automatically when it compiles the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556037">HBAFCPBindingEntry WMI Class</a> in <i>hbaapi.mof</i>. </p>

<p>For an explanation of the fibre channel protocol (FCP), see the T11 committee's <i>Fibre Channel Protocol for SCSI</i> specification. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556037">HBAFCPBindingEntry WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBAFCPBindingEntry structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
