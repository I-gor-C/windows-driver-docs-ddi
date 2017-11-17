---
UID: NS.hbaapi.HBA_FCPBindingEntry2
title: HBA_FCPBindingEntry2
author: windows-driver-content
description: The HBA_FCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.
old-location: storage\hba_fcpbindingentry2.htm
ms.assetid: e2e7353d-2c83-4704-bec4-9485ab3c7706
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
req.alt-api: HBA_FCPBINDINGENTRY2
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
ms.keywords: HBA_FCPBindingEntry2, HBA_FCPBINDINGENTRY2, *PHBA_FCPBINDINGENTRY2
req.iface: 
---

# HBA_FCPBindingEntry2 structure



## -description
<p>The HBA_FCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit.</p>


## -syntax

````
typedef struct HBA_FCPBindingEntry2 {
  HBA_BIND_TYPE type;
  HBA_SCSIID    ScsiId;
  HBA_FCPID     FcpId;
  HBA_LUID      LUID;
  HBA_STATUS    Status;
} HBA_FCPBINDINGENTRY2, *PHBA_FCPBINDINGENTRY2;
````


## -struct-fields
<dl>

### -field <b>type</b>

<dd>
<p>Contains a binding type that indicates how the target is specified in the binding. This member can have any of the following values: </p>
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
<p>Indicates that the target is identified by its fibre channel protocol (FCP) ID. The <b>Fcid</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_WWPN</p>
</td>
<td>
<p>Indicates that the target is identified by its worldwide port name. The <b>PortWWN</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_WWNN</p>
</td>
<td>
<p>Indicates that the fibre channel target device is identified by its worldwide node name. The <b>NodeWWN</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a> structure contains this value.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_BIND_TO_LUID</p>
</td>
<td>
<p>Indicates that the target is identified by its fibre channel logical unit ID. The <b>FcpLun</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a> structure contains this value.</p>
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
<p>For a comparable set of values that define how an HBA specifies targets and logical units in the persistent bindings that it maintains, see the WMI property qualifier <a href="https://msdn.microsoft.com/library/windows/hardware/ff556046">HBA_BIND_TYPE</a>. </p>
<p>For a more detailed description of the values that this member can have, see the T11 committee's <i>Fibre Channel HBA API</i> specification. </p>
</dd>

### -field <b>ScsiId</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557191">HBA_ScsiId</a> that contains the information that uniquely identifies a logical unit for the operating system.</p>
</dd>

### -field <b>FcpId</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a> that contains the FCP identifier for the logical unit and information about the port to be queried for information about the device.</p>
</dd>

### -field <b>LUID</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557091">HBA_LUID</a> that holds a logical unit descriptor for the device that the operating system derives from SCSI inquiry data. </p>
</dd>

### -field <b>Status</b>

<dd>
<p>Contains, on return, a status value that indicates the condition of the HBA. The status values that can be returned in this member correspond to the values associated with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> WMI property qualifier. </p>
</dd>
</dl>

## -remarks
<p>This structure is very similar to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556035">HBAFCPBindingEntry2</a> structure. The only difference is that HBA_FCPBindingEntry2 returns HBA status. </p>

<p>This structure is very similar to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556035">HBAFCPBindingEntry2</a> structure. The only difference is that HBA_FCPBindingEntry2 returns HBA status. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556046">HBA_BIND_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556058">HBA_FCPBindingEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556062">HBA_FcpId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557091">HBA_LUID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557191">HBA_ScsiId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556034">HBAFCPBindingEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556035">HBAFCPBindingEntry2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBA_FCPBindingEntry2 structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
