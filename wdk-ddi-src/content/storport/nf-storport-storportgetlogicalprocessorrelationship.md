---
UID: NF.storport.StorPortGetLogicalProcessorRelationship
title: StorPortGetLogicalProcessorRelationship
author: windows-driver-content
description: The StorPortGetLogicalProcessorRelationship routine returns relationship information for one or more specified types.
old-location: storage\storportgetlogicalprocessorrelationship.htm
old-project: storage
ms.assetid: 32b92771-7f23-492c-a3b0-b10032c9f80a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetLogicalProcessorRelationship
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetLogicalProcessorRelationship
req.alt-loc: storport.h
req.ddi-compliance: StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortGetLogicalProcessorRelationship function



## -description
<p>The <b>StorPortGetLogicalProcessorRelationship</b> routine returns relationship information for one or more specified types. These types include groups, physical packages, and nodes in the host system. The information that is returned includes processor affinity masks that are composed of the logical processors in the host system. These logical processors share the specified relationship types.</p>


## -syntax

````
ULONG StorPortGetLogicalProcessorRelationship(
  _In_     PVOID                                    HwDeviceExtension,
  _In_opt_ PPROCESSOR_NUMBER                        ProcessorNumber,
  _In_     LOGICAL_PROCESSOR_RELATIONSHIP           RelationshipType,
  _Out_    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX Information,
  _Inout_  PULONG                                   Length
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param ProcessorNumber [in, optional]

<dd>
<p>An optional pointer to a processor number for which relationships are to be returned. If this parameter is not provided, information about all processors is returned.</p>
</dd>

### -param RelationshipType [in]

<dd>
<p>The type of relationship to be returned.</p>
</dd>

### -param Information [out]

<dd>
<p>A pointer to a buffer that receives the specified information.</p>
</dd>

### -param Length [in, out]

<dd>
<p>A pointer to the length of the information buffer, in bytes. Upon return, this value receives the number of bytes that are populated with relationship information.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortGetLogicalProcessorRelationship</b>routine returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The operation fails with this return value if one or more of the parameters are invalid, for example, if <i>Information</i> is set to <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The operation fails with this return value if one or more of the parameters are invalid, for example, if the supplied buffer is not large enough to hold the requested information.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_storportirql">StorPortIrql</a>
</td>
</tr>
</table>