---
UID: NS.hbapiwmi._GetFcpTargetMapping_OUT
title: GetFcpTargetMapping_OUT
author: windows-driver-content
description: The GetFcpTargetMapping_OUT structure is used to report the output parameter data of the GetFcpTargetMapping WMI method to the WMI client.
old-location: storage\getfcptargetmapping_out.htm
old-project: storage
ms.assetid: a3a3050a-6fa2-4ace-87f2-41b8364f4d30
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetFcpTargetMapping_OUT, GetFcpTargetMapping_OUT, *PGetFcpTargetMapping_OUT
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
req.alt-api: GetFcpTargetMapping_OUT
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

# GetFcpTargetMapping_OUT structure



## -description
<p>The GetFcpTargetMapping_OUT structure is used to report the output parameter data of the <a href="storage.getfcptargetmapping">GetFcpTargetMapping</a> WMI method to the WMI client. </p>


## -syntax

````
typedef struct _GetFcpTargetMapping_OUT {
  ULONG           HBAStatus;
  ULONG           TotalEntryCount;
  ULONG           OutEntryCount;
  HBAFCPScsiEntry Entry[1];
} GetFcpTargetMapping_OUT, *PGetFcpTargetMapping_OUT;
````


## -struct-fields
<dl>

### -field HBAStatus

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>. </p>
</dd>

### -field TotalEntryCount

<dd>
<p>Indicates the total number of persistent bindings associated with the HBA..</p>
</dd>

### -field OutEntryCount

<dd>
<p>Indicates the total number of mappings retrieved by the <a href="storage.getfcptargetmapping">GetFcpTargetMapping</a> WMI method. This value will be less than or equal to <b>TotalEntryCount</b>. </p>
</dd>

### -field Entry

<dd>
<p>Contains an array of structures of type <a href="..\hbapiwmi\ns-hbapiwmi--hbafcpscsientry.md">HBAFCPScsiEntry</a> that describe an HBA's bindings between operating system and fibre channel protocol (FCP) identifiers. </p>
</dd>
</dl>

## -remarks
<p>The <a href="storage.getfcptargetmapping">GetFcpTargetMapping</a> WMI method reports mappings between the information that uniquely identifies a set of logical units for the operating system and the fibre channel protocol (FCP) identifiers for these logical units.</p>

<p>The WMI tool suite generates a declaration of the GetFcpTargetMapping_OUT structure in <i>Hbapiwmi.h </i>when it compiles the <a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>.</p>

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
<a href="storage.getfcptargetmapping">GetFcpTargetMapping</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
<dt>
<a href="..\hbapiwmi\ns-hbapiwmi--hbafcpscsientry.md">HBAFCPScsiEntry</a>
</dt>
<dt>
<a href="storage.msfc_hbafcpinfo_wmi_class">MSFC_HBAFCPInfo WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GetFcpTargetMapping_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
