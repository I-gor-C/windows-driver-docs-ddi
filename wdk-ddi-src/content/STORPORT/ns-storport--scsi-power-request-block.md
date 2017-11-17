---
UID: NS.storport._SCSI_POWER_REQUEST_BLOCK
title: SCSI_POWER_REQUEST_BLOCK
author: windows-driver-content
description: The SCSI_POWER_REQUEST_BLOCK structure is a special version of a SCSI_REQUEST_BLOCK that is used for power management requests.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location: storage\scsi_power_request_block.htm
ms.assetid: 04981b68-db32-461b-b24b-8b2bf2e53f78
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SCSI_POWER_REQUEST_BLOCK
req.alt-loc: storport.h
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
ms.keywords: SCSI_POWER_REQUEST_BLOCK, SCSI_POWER_REQUEST_BLOCK, *PSCSI_POWER_REQUEST_BLOCK
req.iface: 
req.product: Windows 10 or later.
---

# SCSI_POWER_REQUEST_BLOCK structure



## -description
<p>The <b>SCSI_POWER_REQUEST_BLOCK</b> structure is a special version of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a> that is used for power management requests.</p>


## -syntax

````
typedef struct _SCSI_POWER_REQUEST_BLOCK {
  USHORT                     Length;
  UCHAR                      Function;
  UCHAR                      SrbStatus;
  UCHAR                      SrbPowerFlags;
  UCHAR                      PathId;
  UCHAR                      TargetId;
  UCHAR                      Lun;
  STOR_DEVICE_POWER_STATE    DevicePowerState;
  ULONG                      SrbFlags;
  ULONG                      DataTransferLength;
  ULONG                      TimeOutValue;
  PVOID                      DataBuffer;
  PVOID                      SenseInfoBuffer;
  struct _SCSI_REQUEST_BLOCK  *NextSrb;
  PVOID                      OriginalRequest;
  PVOID                      SrbExtension;
  STOR_POWER_ACTION          PowerAction;
#ifdef _WIN64
  ULONG                      Reserved;
#endif 
  UCHAR                      Reserved5[16];
} SCSI_POWER_REQUEST_BLOCK, *PSCSI_POWER_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The size, in bytes, of the <b>SCSI_POWER_REQUEST_BLOCK</b> structure.</p>
</dd>

### -field <b>Function</b>

<dd>
<p>The operation to perform. For the <b>SCSI_POWER_REQUEST_BLOCK</b> structure, this member is always set to SRB_FUNCTION_POWER.</p>
</dd>

### -field <b>SrbStatus</b>

<dd>
<p>The status of the completed request. This member should be set by the miniport driver before it notifies the Storport driver that the request has completed. A miniport driver notifies the Storport driver that the request has completed by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a> function with the <a href="https://msdn.microsoft.com/abceaf2c-3512-409c-9274-096eab810ab2">RequestComplete</a> notification type.</p>
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a> in the WDK documentation for a list of possible values for this member.</p>
</dd>

### -field <b>SrbPowerFlags</b>

<dd>
<p>The power management flags. Currently, the only flag allowed is SRB_POWER_FLAGS_ADAPTER_REQUEST, which indicates that the power management request is for the adapter. If this flag is set, the miniport driver should ignore the values in the <b>PathId</b>, <b>TargetId</b>, and <b>Lun</b>.  </p>
</dd>

### -field <b>PathId</b>

<dd>
<p>The SCSI port or bus identifier for the request. This value is zero based.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>The target controller or device identifier on the bus.</p>
</dd>

### -field <b>Lun</b>

<dd>
<p>The logical unit number (LUN) of the device.</p>
</dd>

### -field <b>DevicePowerState</b>

<dd>
<p>An enumerator value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff567578">STOR_DEVICE_POWER_STATE</a> that specifies the requested power state of the device.</p>
</dd>

### -field <b>SrbFlags</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>DataTransferLength</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>TimeOutValue</b>

<dd>
<p>The interval, in seconds, that the request can execute before the Storport driver determines that the request has timed out.</p>
</dd>

### -field <b>DataBuffer</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>SenseInfoBuffer</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>NextSrb</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>OriginalRequest</b>

<dd>
<p>Miniport driver should ignore this member.</p>
</dd>

### -field <b>SrbExtension</b>

<dd>
<p>A pointer to the SRB extension. A miniport driver must not use this member if it set <b>SrbExtensionSize</b> to zero in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure. The Storport driver does not initialize the memory that this member points to. The HBA can directly access the data that the miniport driver writes into the SRB extension. A miniport driver can obtain the physical address of the SRB extension by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567095">StorPortGetPhysicalAddress</a> routine. </p>
</dd>

### -field <b>PowerAction</b>

<dd>
<p>An enumerator value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff567587">STOR_POWER_ACTION</a> that specifies the type of system shutdown that is about to occur. This value is meaningful only if the device is moving into the D1, D2, or D3 power state as indicated by the <b>DevicePowerState</b> member. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Reserved5</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>The Storport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557369">HwStorBuildIo</a> to pass SRBs to the miniport driver. <b>HwStorBuildIo</b> should check the <b>Function</b> member of the SRB to determine the type of the SRB. If the <b>Function</b> member is set to SRB_FUNCTION_POWER, the SRB is a structure of type <b>SCSI_POWER_REQUEST_BLOCK</b>.</p>

<p>The Storport driver sends <b>SCSI_POWER_REQUEST_BLOCK</b> requests to a miniport driver to notify the miniport driver of Windows power events that affect storage devices that are connected to the adapter. In the case of a power up event, this request gives the miniport driver an opportunity to initialize itself. In the case of a hibernation or shutdown event, this request gives the miniport driver an opportunity to complete I/O requests and prepare for a power down. The miniport driver can use the value in the <b>PowerAction</b> member of the <b>SCSI_POWER_REQUEST_BLOCK</b> to determine what actions are required. After the miniport driver completes the <b>SCSI_POWER_REQUEST_BLOCK</b> request, the Storport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557274">HwScsiAdapterControl</a> with a control request of <b>ScsiStopAdapter</b> to power down the adapter. The miniport driver reinitialize while processing the SRB_FUNCTION_POWER request, or it can wait and reinitialize when the Storport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557365">HwStorAdapterControl</a> to perform a an <b>ScsiRestartAdapter</b> control request.</p>

<p> When transitioning from the D0 power state to a lower-powered state (D1, D2, or D3) the Storport driver sends a <b>SCSI_POWER_REQUEST_BLOCK</b> request to the miniport driver before the underlying bus driver powers down the adapter. </p>

<p>The following conditions must exist before the Storport driver will send a <b>SCSI_POWER_REQUEST_BLOCK</b> request to the miniport driver:</p>

<p>The adapter is not stopped.</p>

<p>The I/O queue for the adapter is paused.</p>

<p>The adapter hardware is powered up.</p>

<p>The miniport can access the adapter's hardware resources.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557369">HwStorBuildIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567433">StorPortNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20SCSI_POWER_REQUEST_BLOCK structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
