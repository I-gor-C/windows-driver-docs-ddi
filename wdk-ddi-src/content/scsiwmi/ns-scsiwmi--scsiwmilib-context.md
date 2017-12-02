---
UID: NS.scsiwmi._SCSIWMILIB_CONTEXT
title: SCSIWMILIB_CONTEXT
author: windows-driver-content
description: A SCSI_WMILIB_CONTEXT structure provides registration information for a miniport driver's data and event blocks and defines entry points for the miniport driver's HwScsiWmiXxx callback routines.
old-location: storage\scsi_wmilib_context.htm
old-project: storage
ms.assetid: 7886cee8-1142-42e6-8206-84667621ba77
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SCSIWMILIB_CONTEXT, SCSI_WMILIB_CONTEXT, *PSCSI_WMILIB_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: scsiwmi.h
req.include-header: Scsiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSI_WMILIB_CONTEXT
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
req.iface: 
req.product: Windows 10 or later.
---

# SCSIWMILIB_CONTEXT structure



## -description
<p>A SCSI_WMILIB_CONTEXT structure provides registration information for a miniport driver's data and event blocks and defines entry points for the miniport driver's <b>HwScsiWmi</b><b><i>Xxx</i></b> callback routines. </p>


## -syntax

````
typedef struct _SCSIWMILIB_CONTEXT {
  ULONG                     GuidCount;
  PSCSIWMIGUIDREGINFO       GuidList;
  PSCSIWMI_QUERY_REGINFO    QueryWmiRegInfo;
  PSCSIWMI_QUERY_DATABLOCK  QueryWmiDataBlock;
  PSCSIWMI_SET_DATABLOCK    SetWmiDataBlock;
  PSCSIWMI_SET_DATAITEM     SetWmiDataItem;
  PSCSIWMI_EXECUTE_METHOD   ExecuteWmiMethod;
  PSCSIWMI_FUNCTION_CONTROL WmiFunctionControl;
} SCSI_WMILIB_CONTEXT, *PSCSI_WMILIB_CONTEXT;
````


## -struct-fields
<dl>

### -field GuidCount

<dd>
<p>Specifies the number of structures in the SCSIWMIGUIDREGINFO array at <b>GuidList</b>.</p>
</dd>

### -field GuidList

<dd>
<p>Points to an array of <b>GuidCount</b> SCSIWMIGUIDREGINFO structures that contain registration information for each block.</p>
</dd>

### -field QueryWmiRegInfo

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmiqueryreginfo">HwScsiWmiQueryReginfo</a> routine, which is a required entry point for miniport drivers that support WMI.</p>
</dd>

### -field QueryWmiDataBlock

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmiquerydatablock">HwScsiWmiQueryDataBlock</a> routine, which is a required entry point for miniport drivers that support WMI.</p>
</dd>

### -field SetWmiDataBlock

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmisetdatablock">HwScsiWmiSetDataBlock</a> routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to <b>NULL</b></p>
</dd>

### -field SetWmiDataItem

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmisetdataitem">HwScsiWmiSetDataItem</a> routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to <b>NULL</b>.</p>
</dd>

### -field ExecuteWmiMethod

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmiexecutemethod">HwScsiWmiExecuteMethod</a> routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to <b>NULL</b></p>
</dd>

### -field WmiFunctionControl

<dd>
<p>Points to the driver's <a href="storage.hwscsiwmifunctioncontrol">HwScsiWmiFunctionControl</a> routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to <b>NULL</b>. </p>
</dd>
</dl>

## -remarks
<p>A SCSI miniport driver that supports WMI stores an initialized SCSI_WMILIB_CONTEXT structure (or a pointer to such a structure) in its device extension. A miniport driver can use the same SCSI_WMILIB_CONTEXT structure for multiple device objects if each device object supplies the same set of data blocks. </p>

<p>When the miniport driver receives an SRB in which the <b>Function</b> member is set to SRB_FUNCTION_WMI, it calls <a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a> with request parameters, including a pointer to an initialized SCSI_WMILIB_CONTEXT structure. <b>ScsiPortWmiDispatchFunction</b> handles the request by calling the miniport driver's appropriate HwScsiWmiXxx routine.</p>

<p>If the miniport driver does not implement an optional HwScsiWmiXxx routine, the port driver returns an appropriate status to the caller.</p>

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
<a href="storage.hwscsiwmiexecutemethod">HwScsiWmiExecuteMethod</a>
</dt>
<dt>
<a href="storage.hwscsiwmifunctioncontrol">HwScsiWmiFunctionControl</a>
</dt>
<dt>
<a href="storage.hwscsiwmiquerydatablock">HwScsiWmiQueryDataBlock</a>
</dt>
<dt>
<a href="storage.hwscsiwmiqueryreginfo">HwScsiWmiQueryReginfo</a>
</dt>
<dt>
<a href="storage.hwscsiwmisetdatablock">HwScsiWmiSetDataBlock</a>
</dt>
<dt>
<a href="storage.hwscsiwmisetdataitem">HwScsiWmiSetDataItem</a>
</dt>
<dt>
<a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a>
</dt>
<dt>
<a href="storage.scsiwmiguidreginfo">SCSIWMIGUIDREGINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SCSI_WMILIB_CONTEXT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
