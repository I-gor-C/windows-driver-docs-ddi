---
UID: NS.fwpsk._NDIS_SWITCH_NIC_SAVE_STATE
title: NDIS_SWITCH_NIC_SAVE_STATE
author: windows-driver-content
description: The NDIS_SWITCH_NIC_SAVE_STATE structure specifies the run-time state information for a Hyper-V extensible switch port. The extensible switch extension uses this structure to save or restore run-time port information.
old-location: netvista\ndis_switch_nic_save_state.htm
old-project: netvista
ms.assetid: FBC2EE79-9D36-4CA9-A7BC-9C422DE51B13
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_SWITCH_NIC_SAVE_STATE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Ndis.h, Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_NIC_SAVE_STATE
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NDIS_SWITCH_NIC_SAVE_STATE structure



## -description
<p>
<p>The <b>NDIS_SWITCH_NIC_SAVE_STATE</b> structure specifies the run-time state information for a Hyper-V extensible switch port.  The extensible switch extension uses this structure to save or restore run-time port information.</p>
</p>
<p>The <b>NDIS_SWITCH_NIC_SAVE_STATE</b> structure specifies the run-time state information for a Hyper-V extensible switch port.  The extensible switch extension uses this structure to save or restore run-time port information.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_NIC_SAVE_STATE {
  NDIS_OBJECT_HEADER                 Header;
  ULONG                              Flags;
  NDIS_SWITCH_NIC_INDEX              NicIndex;
  NDIS_SWITCH_PORT_ID                PortId;
  GUID                               ExtensionId;
  NDIS_SWITCH_EXTENSION_FRIENDLYNAME ExtensionFriendlyName;
  GUID                               FeatureClassId;
  USHORT                             SaveDataSize;
  USHORT                             SaveDataOffset;
} NDIS_SWITCH_NIC_SAVE_STATE, *PNDIS_SWITCH_NIC_SAVE_STATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_NIC_SAVE_STATE</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_NIC_SAVE_STATE</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_NIC_SAVE_STATE_REVISION_1"></a><a id="ndis_switch_nic_save_state_revision_1"></a>NDIS_SWITCH_NIC_SAVE_STATE_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_NIC_SAVE_STATE_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>NicIndex</b>

<dd>
<p>An NDIS_SWITCH_NIC_INDEX  value that contains the Nic Index for the network adapter. This value will always be 0. For more information, see <a href="NULL">Network Adapter Index Values</a>.</p>
</dd>

### -field <b>PortId</b>

<dd>
<p>An NDIS_SWITCH_PORT_ID value that contains the unique identifier of the extensible switch port.</p>
</dd>

### -field <b>ExtensionId</b>

<dd>
<p>A GUID value that identifies the extensible switch extension.</p>
</dd>

### -field <b>ExtensionFriendlyName</b>

<dd>
<p> An NDIS_SWITCH_EXTENSION_FRIENDLYNAME value that specifies the user-friendly description of the extensible switch extension.</p>
</dd>

### -field <b>FeatureClassId</b>

<dd>
<p>A GUID value that contains the identifier of the feature class related to the saved data. A feature class identifier is defined by the extension to uniquely identify components of its run-time data.</p>
<div class="alert"><b>Note</b>  This member is optional. The extensible switch extension must set this member to 0 if the saved data has no feature class.</div>
<div> </div>
</dd>

### -field <b>SaveDataSize</b>

<dd>
<p>A USHORT value that specified the size, in bytes, of the data that is contained in the <b>SaveData</b> member.</p>
<div class="alert"><b>Note</b>  This value must be less than or equal to NDIS_SWITCH_NIC_SAVE_STATE_MAX_DATA_SIZE.</div>
<div> </div>
</dd>

### -field <b>SaveDataOffset</b>

<dd>
<p>A USHORT value that contains the offset from the start of the structure to the run-time state information being saved or restored.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_NIC_SAVE_STATE</b> structure is used in the following OID requests: </p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598268">OID_SWITCH_NIC_SAVE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598269">OID_SWITCH_NIC_SAVE_COMPLETE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598267">OID_SWITCH_NIC_RESTORE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh846215">OID_SWITCH_NIC_RESTORE_COMPLETE</a>
</p>

<p>For more information on how to save or restore run-time port information, see <a href="NULL">Managing Hyper-V Extensible Switch Run-Time Data</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h or Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451419">IF_COUNTED_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598267">OID_SWITCH_NIC_RESTORE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598268">OID_SWITCH_NIC_SAVE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598269">OID_SWITCH_NIC_SAVE_COMPLETE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_NIC_SAVE_STATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
