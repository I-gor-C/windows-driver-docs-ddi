---
UID: NS.scsiwmi.PSCSIWMIGUIDREGINFO
title: PSCSIWMIGUIDREGINFO
author: windows-driver-content
description: The SCSIWMIGUIDREGINFO structure contains information about a given data or event block supported by a SCSI miniport driver.
old-location: storage\scsiwmiguidreginfo.htm
ms.assetid: 7116445e-751b-478a-8e58-8f5c90d06b9b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsiwmi.h
req.include-header: Scsiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSIWMIGUIDREGINFO
req.alt-loc: scsiwmi.h
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
ms.keywords: PSCSIWMIGUIDREGINFO, SCSIWMIGUIDREGINFO, *PSCSIWMIGUIDREGINFO
req.iface: 
req.product: Windows 10 or later.
---

# PSCSIWMIGUIDREGINFO structure



## -description
<p>The SCSIWMIGUIDREGINFO structure contains information about a given data or event block supported by a SCSI miniport driver. </p>


## -syntax

````
typedef struct {
  LPCGUID Guid;
  ULONG   InstanceCount;
  ULONG   Flags;
} SCSIWMIGUIDREGINFO, *PSCSIWMIGUIDREGINFO;
````


## -struct-fields
<dl>

### -field <b>Guid</b>

<dd>
<p>Points to the GUID that identifies the block. </p>
</dd>

### -field <b>InstanceCount</b>

<dd>
<p>Specifies the number of instances defined for the block.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Indicates characteristics of the block. The SCSI port driver sets all but the following WMIREG_FLAG_<i>XXX</i> on behalf of the miniport driver. A miniport driver might set one or more of the following flags: </p>
<p></p>
<dl>

### -field <a id="WMIREG_FLAG_EVENT_ONLY_GUID"></a><a id="wmireg_flag_event_only_guid"></a>WMIREG_FLAG_EVENT_ONLY_GUID

<dd>
<p>The block can be enabled or disabled as an event only, and cannot be queried or set. If this flag is clear, the block can also be queried or set. </p>
</dd>

### -field <a id="WMIREG_FLAG_EXPENSIVE"></a><a id="wmireg_flag_expensive"></a>WMIREG_FLAG_EXPENSIVE

<dd>
<p>Requests the port driver send an enable-collection SRB the first time a data consumer opens the data block and a disable-collection SRB when the last data consumer closes the data block. This is recommended if collecting such data affects performance. A miniport driver need not collect the data until a data consumer explicitly requests it by opening the block. </p>
</dd>

### -field <a id="WMIREG_FLAG_REMOVE_GUID"></a><a id="wmireg_flag_remove_guid"></a>WMIREG_FLAG_REMOVE_GUID

<dd>
<p>Removes support for a previously registered block when set.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The miniport driver passes a pointer to a SCSI_WMILIB_CONTEXT which contains a SCSIWMIREGGUID array in the <i>WmiLibInfo</i> parameter of <a href="https://msdn.microsoft.com/library/windows/hardware/ff564766">ScsiPortWmiDispatchFunction</a>. The miniport driver passes this information each time it calls <b>ScsiPortWmiDispatchFunction</b>. Each SCSIWMIREGGUID structure in the array represents one of the miniport driver's data or event blocks. </p>

<p>A miniport driver's SCSIWMIREGGUID array should include any standard data blocks defined in <i>wmicore.mof</i> for its device type, and might include miniport driver-defined data and event blocks. A miniport driver defines custom data and event blocks in a MOF file, which is compiled as a resource attached to the miniport driver's binary image and specified in the <i>MofResourceName</i> parameter of the miniport driver's HwScsiWmiQueryReginfo routine. </p>

<p>For more information about defining blocks, <a href="https://msdn.microsoft.com/5c2ed322-0fc9-4004-9a5f-f4d3c6a59fe9">Windows Management Instrumentation</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsiwmi.h (include Scsiwmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557344">HwScsiWmiQueryReginfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565395">SCSI_WMILIB_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564766">ScsiPortWmiDispatchFunction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20SCSIWMIGUIDREGINFO structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
