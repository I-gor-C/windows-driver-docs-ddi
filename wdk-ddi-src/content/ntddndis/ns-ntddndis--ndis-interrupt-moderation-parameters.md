---
UID: NS.ntddndis._NDIS_INTERRUPT_MODERATION_PARAMETERS
title: NDIS_INTERRUPT_MODERATION_PARAMETERS
author: windows-driver-content
description: The NDIS_INTERRUPT_MODERATION_PARAMETERS structure defines interrupt parameters for the OID_GEN_INTERRUPT_MODERATION OID.
old-location: netvista\ndis_interrupt_moderation_parameters.htm
old-project: netvista
ms.assetid: e2270dbc-0bc3-4bef-9e11-26006d8f0d71
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_INTERRUPT_MODERATION_PARAMETERS, NDIS_INTERRUPT_MODERATION_PARAMETERS, *PNDIS_INTERRUPT_MODERATION_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_INTERRUPT_MODERATION_PARAMETERS
req.alt-loc: ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_INTERRUPT_MODERATION_PARAMETERS structure



## -description
<p>The NDIS_INTERRUPT_MODERATION_PARAMETERS structure defines interrupt parameters for the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff569590">OID_GEN_INTERRUPT_MODERATION</a> OID.
  
  </p>


## -syntax

````
typedef struct _NDIS_INTERRUPT_MODERATION_PARAMETERS {
  NDIS_OBJECT_HEADER        Header;
  ULONG                     Flags;
  NDIS_INTERRUPT_MODERATION InterruptModeration;
} NDIS_INTERRUPT_MODERATION_PARAMETERS, *PNDIS_INTERRUPT_MODERATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_INTERRUPT_MODERATION_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_INTERRUPT_MODERATION_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_INTERRUPT_MODERATION_PARAMETERS_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of the following flags:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_INTERRUPT_MODERATION_CHANGE_NEEDS_RESET"></a><a id="ndis_interrupt_moderation_change_needs_reset"></a>NDIS_INTERRUPT_MODERATION_CHANGE_NEEDS_RESET

<dd>
<p>A network interface card (NIC) must have a hardware reset to enable or disable interrupt
       moderation.</p>
</dd>

### -field <a id="NDIS_INTERRUPT_MODERATION_CHANGE_NEEDS_REINITIALIZE"></a><a id="ndis_interrupt_moderation_change_needs_reinitialize"></a>NDIS_INTERRUPT_MODERATION_CHANGE_NEEDS_REINITIALIZE

<dd>
<p>A miniport driver must complete a halt and reinitialize cycle to enable or disable interrupt
       moderation. If this flag is enabled, there is also a hardware reset.</p>
</dd>
</dl>
</dd>

### -field <b>InterruptModeration</b>

<dd>
<p>An NDIS_INTERRUPT_MODERATION-typed value that indicates or specifies the current interrupt
     moderation status.
     </p>
<p>The following values are supported:</p>
<p></p>
<dl>

### -field <a id="NdisInterruptModerationUnknown"></a><a id="ndisinterruptmoderationunknown"></a><a id="NDISINTERRUPTMODERATIONUNKNOWN"></a><b>NdisInterruptModerationUnknown</b>

<dd>
<p>In an OID query, this value indicates that the miniport driver cannot determine whether
       interrupt moderation is enabled or disabled on a NIC. This value is invalid for a set request.</p>
</dd>

### -field <a id="NdisInterruptModerationNotSupported"></a><a id="ndisinterruptmoderationnotsupported"></a><a id="NDISINTERRUPTMODERATIONNOTSUPPORTED"></a><b>NdisInterruptModerationNotSupported</b>

<dd>
<p>In an OID query, this value indicates that the NIC or its miniport driver does not support
       interrupt moderation. This value is invalid for a set request.</p>
</dd>

### -field <a id="NdisInterruptModerationEnabled"></a><a id="ndisinterruptmoderationenabled"></a><a id="NDISINTERRUPTMODERATIONENABLED"></a><b>NdisInterruptModerationEnabled</b>

<dd>
<p>In an OID query, this value indicates that interrupt moderation is enabled on the NIC. In an OID
       set, 
       <b>NdisInterruptModerationEnabled</b> indicates that interrupt moderation should be enabled on the
       NIC.</p>
</dd>

### -field <a id="NdisInterruptModerationDisabled"></a><a id="ndisinterruptmoderationdisabled"></a><a id="NDISINTERRUPTMODERATIONDISABLED"></a><b>NdisInterruptModerationDisabled</b>

<dd>
<p>In an OID query, this value indicates that interrupt moderation is disabled on the NIC. In an
       OID set, 
       <b>NdisInterruptModerationDisabled</b> indicates that interrupt moderation should be disabled on the
       NIC.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The NDIS_INTERRUPT_MODERATION_PARAMETERS structure defines interrupt parameters for the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569590">OID_GEN_INTERRUPT_MODERATION</a> OID
    query and set operations. Only the 
    <b>NdisInterruptModerationEnabled</b> and 
    <b>NdisInterruptModerationDisabled</b> values for the 
    <b>InterruptModeration</b> member apply to set operations.</p>

<p>The NDIS_INTERRUPT_MODERATION_PARAMETERS structure defines interrupt parameters for the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569590">OID_GEN_INTERRUPT_MODERATION</a> OID
    query and set operations. Only the 
    <b>NdisInterruptModerationEnabled</b> and 
    <b>NdisInterruptModerationDisabled</b> values for the 
    <b>InterruptModeration</b> member apply to set operations.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569590">OID_GEN_INTERRUPT_MODERATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_INTERRUPT_MODERATION_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
