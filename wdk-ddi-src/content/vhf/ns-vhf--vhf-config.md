---
UID: NS.vhf._VHF_CONFIG
title: VHF_CONFIG
author: windows-driver-content
description: Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device.
old-location: hid\vhf_config.htm
ms.assetid: 384BE20B-0F40-418D-B24E-9711BF7CE53A
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: hid
req.header: vhf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VHF_CONFIG
req.alt-loc: vhf.h
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
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# VHF_CONFIG structure



## -description
<p>Contains initial configuration information that is provided by the HID source driver when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/dn925036">VhfCreate</a> to create a virtual HID device.</p>


## -syntax

````
typedef struct _VHF_CONFIG {
  ULONG                                            Size;
  PVOID                                            VhfClientContext;
  ULONG                                            OperationContextSize;
  PDEVICE_OBJECT                                   DeviceObject;
  USHORT                                           VendorID;
  USHORT                                           ProductID;
  USHORT                                           VersionNumber;
  GUID                                             ContainerID;
  USHORT                                           ReportDescriptorLength;
  _Field_size_full_(ReportDescriptorLength) PUCHAR ReportDescriptor;
  PEVT_VHF_READY_FOR_NEXT_READ_REPORT              EvtVhfReadyForNextReadReport;
  PEVT_VHF_ASYNC_OPERATION                         EvtVhfAsyncOperationGetFeature;
  PEVT_VHF_ASYNC_OPERATION                         EvtVhfAsyncOperationSetFeature;
  PEVT_VHF_ASYNC_OPERATION                         EvtVhfAsyncOperationWriteReport;
  PEVT_VHF_ASYNC_OPERATION                         EvtVhfAsyncOperationGetInputReport;
  PEVT_VHF_CLEANUP                                 EvtVhfCleanup;
} VHF_CONFIG, *PVHF_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Required. Size of this structure initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/dn925046">VHF_CONFIG_INIT</a>.</p>
</dd>

### -field <b>VhfClientContext</b>

<dd>
<p>Optional. An opaque pointer to HID source driver-allocated memory that the Virtual HID Framework (VHF) passes when it invokes  those callback functions.</p>
</dd>

### -field <b>OperationContextSize</b>

<dd>
<p>Optional. Size of the buffer that VHF must allocate for an asynchronous operation started by <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a>. If non-zero, VHF allocates a buffer of this size and passes a pointer to that buffer in the <i>VhfOperationContext</i> parameter each time it invokes <i>EvtVhfAsyncOperation</i> to start a new operation.</p>
</dd>

### -field <b>DeviceObject</b>

<dd>
<p>Required. A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure for the HID source driver. Get that pointer by calling  <a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a> and passing the WDFDEVICE handle that the driver received in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> call. </p>
</dd>

### -field <b>VendorID</b>

<dd>
<p>Optional. Vendor ID of the virtual HID device to be created.</p>
</dd>

### -field <b>ProductID</b>

<dd>
<p>Optional. Product ID of the virtual HID device to be created.</p>
</dd>

### -field <b>VersionNumber</b>

<dd>
<p>Optional. Version number of the virtual HID device to be created.</p>
</dd>

### -field <b>ContainerID</b>

<dd>
<p>Optional. Container ID of the virtual HID device to be created.</p>
</dd>

### -field <b>ReportDescriptorLength</b>

<dd>
<p>Required. The length of the HID Report Descriptor contained in a buffer pointed by <b>ReportDescriptor</b>.</p>
</dd>

### -field <b>ReportDescriptor</b>

<dd>
<p>Required. A pointer to a HID source driver-allocated buffer that contains the  HID Report Descriptor.</p>
</dd>

### -field <b>EvtVhfReadyForNextReadReport</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/02DDBE00-C342-474B-8D06-FBB929BA4760">EvtVhfReadyForNextReadReport</a> callback. The HID source driver must implement and register this callback function if it wants to handle the buffering policy for submitting HID Input Reports. If this callback is specified, VHF does not buffer those reports. The HID source driver should submit one report by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn925040">VhfReadReportSubmit</a>, each time VHF invokes   <i>EvtVhfReadyForNextReadReport</i>.</p>
</dd>

### -field <b>EvtVhfAsyncOperationGetFeature</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a get a HID Feature Report associated with a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">Top-Level Collection</a> from the HID class driver pair.
The driver can get a Feature Report only if the Report Descriptor declares it.</p>
</dd>

### -field <b>EvtVhfAsyncOperationSetFeature</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a send  a HID Feature Report associated with a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">Top-Level Collection</a> to the HID class driver pair. The driver can set a Feature Report only if the Report Descriptor declares it.</p>
</dd>

### -field <b>EvtVhfAsyncOperationWriteReport</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a support HID Output Reports and send  them to the  HID class driver pair. </p>
</dd>

### -field <b>EvtVhfAsyncOperationGetInputReport</b>

<dd>
<p>Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to support on-demand query for Input Reports.</p>
</dd>

### -field <b>EvtVhfCleanup</b>

<dd>
<p>Optional. A pointer to a <a href="https://msdn.microsoft.com/1D477E7B-E4EA-46E7-872C-3BEBFBD31702">EvtVhfCleanup</a> callback. The HID source driver can implement and register this callback function if it wants to free the allocated resources for the virtual HID device. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Vhf.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Write a HID source driver by using Virtual HID Framework (VHF)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20VHF_CONFIG structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
