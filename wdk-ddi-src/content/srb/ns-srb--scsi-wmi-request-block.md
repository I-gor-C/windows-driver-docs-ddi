---
UID: NS.srb._SCSI_WMI_REQUEST_BLOCK
title: SCSI_WMI_REQUEST_BLOCK
author: windows-driver-content
description: This structure is a special version of a SCSI_REQUEST_BLOCK for use with WMI commands.
old-location: storage\scsi_wmi_request_block.htm
old-project: storage
ms.assetid: 6dc10c3a-b47e-42c3-a209-34977fb219f1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SCSI_WMI_REQUEST_BLOCK, SCSI_WMI_REQUEST_BLOCK, *PSCSI_WMI_REQUEST_BLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: srb.h
req.include-header: Storport.h, Srb.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSI_WMI_REQUEST_BLOCK
req.alt-loc: srb.h
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

# SCSI_WMI_REQUEST_BLOCK structure



## -description
<p>This structure is a special version of a <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> for use with WMI commands. </p>


## -syntax

````
typedef struct _SCSI_WMI_REQUEST_BLOCK {
  USHORT Length;
  UCHAR  Function;
  UCHAR  SrbStatus;
  UCHAR  WMISubFunction;
  UCHAR  PathId;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  Reserved1;
  UCHAR  WMIFlags;
  UCHAR  Reserved2[2];
  ULONG  SrbFlags;
  ULONG  DataTransferLength;
  ULONG  TimeOutValue;
  PVOID  DataBuffer;
  PVOID  DataPath;
  PVOID  Reserved3;
  PVOID  OriginalRequest;
  PVOID  SrbExtension;
  ULONG  Reserved4;
#ifdef _WIN64
  ULONG  Reserved6;
#endif 
  UCHAR  Reserved5[16];
} SCSI_WMI_REQUEST_BLOCK, *PSCSI_WMI_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>Function</b>

<dd>
<p>SRB_FUNCTION_WMI, which specifies that the request is a WMI request. If this member is not set to SRB_FUNCTION_WMI, the miniport driver should fail the request.</p>
</dd>

### -field <b>SrbStatus</b>

<dd>
<p>Returns the status of the completed request. This member should be set by the miniport driver before it notifies the OS-specific driver that the request has completed by calling <a href="..\srb\nf-srb-scsiportnotification.md">ScsiPortNotification</a> with <b>RequestComplete</b>. The value of this member can be any value listed for <b>SrbStatus</b> in SCSI_REQUEST_BLOCK.</p>
</dd>

### -field <b>WMISubFunction</b>

<dd>
<p>Indicates the WMI action to be performed. A miniport driver calls <a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a> with <i>MinorFunction</i> set to this value. The subfunction value corresponds to the WMI minor IRP number that identifies the WMI operation. </p>
</dd>

### -field <b>PathId</b>

<dd>
<p>Indicates the SCSI port or bus for the request. This value is zero-based. If SRB_WMI_FLAGS_ADAPTER_REQUEST is set in <b>WMIFlags</b>, this member is reserved.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>Indicates the target controller or device on the bus. If SRB_WMI_FLAGS_ADAPTER_REQUEST is set in <b>WMIFlags</b>, this member is reserved.</p>
</dd>

### -field <b>Lun</b>

<dd>
<p>Indicates the logical unit number of the device. If SRB_WMI_FLAGS_ADAPTER_REQUEST is set in <b>WMIFlags</b>, this member is reserved.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>WMIFlags</b>

<dd>
<p>Indicates that the WMI request is for the adapter if SRB_WMI_FLAGS_ADAPTER_REQUEST is set and that <b>PathId</b>, <b>TargetId</b>, and <b>Lun</b> are reserved. Otherwise, <b>WMIFlags</b> will be <b>NULL</b>, indicating that the request is for the device specified by <b>PathId</b>, <b>TargetId</b>, and <b>Lun</b>.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>SrbFlags</b>

<dd>
<p>Indicates various parameters and options about the request. <b>SrbFlags</b> is read-only. This member will be set to one or more of the following flags ORed together:</p>
<p></p>
<dl>

### -field <a id="SRB_FLAGS_DATA_IN"></a><a id="srb_flags_data_in"></a>SRB_FLAGS_DATA_IN

<dd>
<p>Indicates data will be transferred from the device to the system.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="SRB_FLAGS_DATA_OUT"></a><a id="srb_flags_data_out"></a>SRB_FLAGS_DATA_OUT

<dd>
<p>Indicates data will be transferred from the system to the device.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="SRB_FLAGS_NO_DATA_TRANSFER"></a><a id="srb_flags_no_data_transfer"></a>SRB_FLAGS_NO_DATA_TRANSFER

<dd>
<p>Indicates no data transfer with this request. If this is set, the flags SRB_FLAGS_DATA_OUT, SRB_FLAGS_DATA_IN, and SRB_FLAGS_UNSPECIFIED_DIRECTION are clear.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="SRB_FLAGS_DISABLE_SYNCH_TRANSFER"></a><a id="srb_flags_disable_synch_transfer"></a>SRB_FLAGS_DISABLE_SYNCH_TRANSFER

<dd>
<p>Indicates the HBA, if possible, should perform asynchronous I/O for this transfer request. If synchronous I/O was negotiated previously, the HBA must renegotiate for asynchronous I/O before performing the transfer.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="SRB_FLAGS_DISABLE_DISCONNECT"></a><a id="srb_flags_disable_disconnect"></a>SRB_FLAGS_DISABLE_DISCONNECT

<dd>
<p>Indicates the HBA should not allow the target to disconnect from the SCSI bus during processing of this request.</p>
</dd>
</dl>
</dd>

### -field <b>DataTransferLength</b>

<dd>
<p>Indicates the size in bytes of the data buffer. A miniport driver calls <a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a> with <i>BufferSize</i> set to this value. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.</p>
</dd>

### -field <b>TimeOutValue</b>

<dd>
<p>Indicates the interval in seconds that the request can execute before the OS-specific port driver might consider it timed out. Miniport drivers are not required to time requests because the port driver already does.</p>
</dd>

### -field <b>DataBuffer</b>

<dd>
<p>Points to the data buffer. A miniport driver calls <a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a> with <i>Buffer</i> set to this value. Miniport drivers can use this value as a data pointer regardless of the value of <b>MapBuffers</b> in the PORT_CONFIGURATION_INFORMATION for the HBA. A miniport driver cannot transfer data directly into the buffer using DMA.</p>
</dd>

### -field <b>DataPath</b>

<dd>
<p>Specifies the WMI data path for this request. A miniport driver calls <a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a> with <i>DataPath</i> set to this value. </p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>OriginalRequest</b>

<dd>
<p>Points to the IRP for this request. This member is irrelevant to miniport drivers.</p>
</dd>

### -field <b>SrbExtension</b>

<dd>
<p>Points to the Srb extension. A miniport driver must not use this member if it set <b>SrbExtensionSize</b> to zero in the HW_INITIALIZATION_DATA. The memory at <b>SrbExtension</b> is not initialized by the OS-specific port driver, and the miniport driver-determined data can be accessed directly by the HBA. The corresponding physical address can be obtained by calling <a href="..\srb\nf-srb-scsiportgetphysicaladdress.md">ScsiPortGetPhysicalAddress</a> with the <b>SrbExtension</b> pointer.</p>
</dd>

### -field <b>Reserved4</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>

### -field <b>Reserved6</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers. This member is valid starting with Windows Server 2003 with SP1.</p>
</dd>

### -field <b>Reserved5</b>

<dd>
<p>Reserved for system use and not available for use by miniport drivers.</p>
</dd>
</dl>

## -remarks
<p>Windows NT storage class and filter drivers can send WMI SRBs to the system port driver. The system port driver will handle certain WMI requests on behalf of miniport drivers. If the port driver cannot handle a WMI request, it forwards the request to the miniport driver. </p>

<p>A miniport driver receives WMI requests from the port driver only if the miniport driver set <b>WmiDataProvider</b> in the PORT_CONFIGURATION_INFORMATION structure. If the miniport driver supports a request, it should process it and complete the request by calling <b>ScsiPortNotification</b> twice, first with <b>RequestComplete</b> and then with <b>NextRequest</b> (or <b>NextLuRequest</b>). </p>

<p>For information about supporting WMI in miniport drivers, see the <a href="https://msdn.microsoft.com/5c2ed322-0fc9-4004-9a5f-f4d3c6a59fe9">Windows Management Instrumentation</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.hw_initialization_data__scsi_">HW_INITIALIZATION_DATA (SCSI)</a>
</dt>
<dt>
<a href="storage.port_configuration_information__scsi_">PORT_CONFIGURATION_INFORMATION (SCSI)</a>
</dt>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="..\srb\nf-srb-scsiportnotification.md">ScsiPortNotification</a>
</dt>
<dt>
<a href="..\scsiwmi\nf-scsiwmi-scsiportwmidispatchfunction.md">ScsiPortWmiDispatchFunction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SCSI_WMI_REQUEST_BLOCK structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
