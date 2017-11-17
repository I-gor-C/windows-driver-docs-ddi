---
UID: NS.ntddscsi._NVCACHE_REQUEST_BLOCK
title: NVCACHE_REQUEST_BLOCK
author: windows-driver-content
description: The NVCACHE_REQUEST_BLOCK structure is used in conjunction with the IOCTL_SCSI_MINIPORT request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology).
old-location: storage\nvcache_request_block.htm
ms.assetid: 25ca2d81-72a5-47ae-bdfd-0ec63e1ca39a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NVCACHE_REQUEST_BLOCK
req.alt-loc: ntddscsi.h
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
ms.keywords: NVCACHE_REQUEST_BLOCK, NVCACHE_REQUEST_BLOCK, *PNVCACHE_REQUEST_BLOCK
req.iface: 
---

# NVCACHE_REQUEST_BLOCK structure



## -description
<p>The <b>NVCACHE_REQUEST_BLOCK</b> structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560512">IOCTL_SCSI_MINIPORT</a> request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology). This topic defines the general structure for both input data and output data for a call made to the NV Cache Manager. A caller should fill all required fields before calling <a href="base.deviceiocontrol">DeviceIoControl</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548318">IoBuildDeviceIoControlRequest</a>. The miniport driver must do the same after the requested function is completed, and before it returns.</p>


## -syntax

````
typedef struct _NVCACHE_REQUEST_BLOCK {
  ULONG     NRBSize;
  USHORT    Function;
  ULONG     NRBFlags;
  ULONG     NRBStatus;
  ULONG     Count;
  ULONGLONG LBA;
  ULONG     DataBufSize;
  ULONG     NVCacheStatus;
  ULONG     NVCacheSubStatus;
} NVCACHE_REQUEST_BLOCK, *PNVCACHE_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field <b>NRBSize</b>

<dd>
<p>The <b>sizeof</b>(NVCACHE_REQUEST_BLOCK).</p>
</dd>

### -field <b>Function</b>

<dd>
<p>Specifies the operation to be performed, which can be one of the following values:</p>
<p></p>
<dl>

### -field <a id="NRB_FUNCTION_NVCACHE_INFO"></a><a id="nrb_function_nvcache_info"></a>NRB_FUNCTION_NVCACHE_INFO

<dd>
<p>Get NV Cache Manager feature support information from the device. Upon the successful completion of this function, the required data fields are returned to the caller. The return data structure is <a href="https://msdn.microsoft.com/library/windows/hardware/ff563248">NV_FEATURE_PARAMETER</a>.</p>
</dd>

### -field <a id="NRB_FUNCTION_SPINDLE_STATUS"></a><a id="nrb_function_spindle_status"></a>NRB_FUNCTION_SPINDLE_STATUS

<dd>
<p>Determine if the device is currently spinning up or spinning down. For an ATA device, a Check Power Mode command is required to obtain the device's spindle status. For a SCSI device, a Mode Sense command can be used to query the device's current power mode.</p>
</dd>

### -field <a id="NRB_FUNCTION_NVCACHE_POWER_MODE_SET"></a><a id="nrb_function_nvcache_power_mode_set"></a>NRB_FUNCTION_NVCACHE_POWER_MODE_SET

<dd>
<p>Turn on the NV Cache Manager power mode.</p>
</dd>

### -field <a id="NRB_FUNCTION_NVCACHE_POWER_MODE_RESET"></a><a id="nrb_function_nvcache_power_mode_reset"></a>NRB_FUNCTION_NVCACHE_POWER_MODE_RESET

<dd>
<p>Turn off the NV Cache Manager power mode.</p>
</dd>

### -field <a id="NRB_FUNCTION_FLUSH_NVCACHE"></a><a id="nrb_function_flush_nvcache"></a>NRB_FUNCTION_FLUSH_NVCACHE

<dd>
<p>Flush the data that is currently pinned in NV cache memory to make the required NV cache memory space available.</p>
</dd>

### -field <a id="NRB_FUNCTION_QUERY_PINNED_SET"></a><a id="nrb_function_query_pinned_set"></a>NRB_FUNCTION_QUERY_PINNED_SET

<dd>
<p>Get the Logical Block Address (LBA) ranges currently in the NV Cache Manager pinned set.</p>
</dd>

### -field <a id="NRB_FUNCTION_QUERY_CACHE_MISS"></a><a id="nrb_function_query_cache_miss"></a>NRB_FUNCTION_QUERY_CACHE_MISS

<dd>
<p>Request that the device report NV Cache Misses in LBA ranges in a single 512-byte block.</p>
</dd>

### -field <a id="NRB_FUNCTION_ADD_LBAS_PINNED_SET"></a><a id="nrb_function_add_lbas_pinned_set"></a>NRB_FUNCTION_ADD_LBAS_PINNED_SET

<dd>
<p>Add the LBAs that are specified in the NV Cache Manager Set Data to the NV Cache Manager Pinned Set if they are not already.</p>
</dd>

### -field <a id="NRB_FUNCTION_REMOVE_LBAS_PINNED_SET"></a><a id="nrb_function_remove_lbas_pinned_set"></a>NRB_FUNCTION_REMOVE_LBAS_PINNED_SET

<dd>
<p>Remove the LBAs that are specified in the NV Cache Set Data from the NV Cache pinned set.</p>
</dd>

### -field <a id="NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS"></a><a id="nrb_function_query_hybrid_disk_status"></a>NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="NRB_FUNCTION_PASS_HINT_PAYLOAD"></a><a id="nrb_function_pass_hint_payload"></a>NRB_FUNCTION_PASS_HINT_PAYLOAD

<dd>
<p>Pass IO hints to a SATA device.</p>
</dd>
</dl>
</dd>

### -field <b>NRBFlags</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>NRBStatus</b>

<dd>
<p>Indicates the NV Cache Manager function request status from the driver. There are seven possible values for this field:</p>
<p></p>
<dl>

### -field <a id="NRB_SUCCESS"></a><a id="nrb_success"></a>NRB_SUCCESS

<dd>
<p>No error.</p>
</dd>

### -field <a id="NRB_ILLEGAL_REQUEST"></a><a id="nrb_illegal_request"></a>NRB_ILLEGAL_REQUEST

<dd>
<p>Illegal request detected by the port driver.</p>
</dd>

### -field <a id="NRB_INVALID_PARAMETER"></a><a id="nrb_invalid_parameter"></a>NRB_INVALID_PARAMETER

<dd>
<p>Invalid parameter passed to the port driver.</p>
</dd>

### -field <a id="NRB_INPUT_DATA_OVERRUN"></a><a id="nrb_input_data_overrun"></a>NRB_INPUT_DATA_OVERRUN

<dd>
<p>Too much data provided to the port driver.</p>
</dd>

### -field <a id="NRB_INPUT_DATA_UNDERRUN"></a><a id="nrb_input_data_underrun"></a>NRB_INPUT_DATA_UNDERRUN

<dd>
<p>Not enough data provided to the port driver.</p>
</dd>

### -field <a id="NRB_OUTPUT_DATA_OVERRUN"></a><a id="nrb_output_data_overrun"></a>NRB_OUTPUT_DATA_OVERRUN

<dd>
<p>Too much data returned from the port driver.</p>
</dd>

### -field <a id="NRB_OUTPUT_DATA_UNDERRUN"></a><a id="nrb_output_data_underrun"></a>NRB_OUTPUT_DATA_UNDERRUN

<dd>
<p>Not enough data returned from the port driver.</p>
</dd>
</dl>
</dd>

### -field <b>Count</b>

<dd>
<p>Number of 512-byte blocks to be transferred with the specified function.</p>
</dd>

### -field <b>LBA</b>

<dd>
<p>Starting LBA of the device for the specified function.</p>
</dd>

### -field <b>DataBufSize</b>

<dd>
<p>Size of the data buffer, in bytes.</p>
</dd>

### -field <b>NVCacheStatus</b>

<dd>
<p>Status returned from the device. For an ATA device, this value is the contents of the Status Register in its Task File. For a SCSI device, this value is the Sense Code returned from the device.</p>
</dd>

### -field <b>NVCacheSubStatus</b>

<dd>
<p>The error code returned from the device. For an ATA device, this value is the contents of the Error Register in its Task File. For a SCSI device, this value is the Sense key returned from the device.</p>
</dd>
</dl>

## -remarks
<p>For more information on function behavior, see section 7.20 of the <a href="http://go.microsoft.com/fwlink/p/?linkid=74996">ATA8-ACS specification</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddscsi.h (include Ntddscsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560512">IOCTL_SCSI_MINIPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560517">IOCTL_SCSI_MINIPORT_NVCACHE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20NVCACHE_REQUEST_BLOCK structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
