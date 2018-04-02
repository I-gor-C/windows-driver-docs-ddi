---
UID: NS:vhf._VHF_CONFIG
title: "_VHF_CONFIG"
author: windows-driver-content
description: Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device.
old-location: hid\vhf_config.htm
old-project: hid
ms.assetid: 384BE20B-0F40-418D-B24E-9711BF7CE53A
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PVHF_CONFIG, PVHF_CONFIG, PVHF_CONFIG structure pointer [Human Input Devices], VHF_CONFIG, VHF_CONFIG structure [Human Input Devices], _VHF_CONFIG, hid.vhf_config, vhf/PVHF_CONFIG, vhf/VHF_CONFIG"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: vhf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	vhf.h
api_name:
-	VHF_CONFIG
product:
- Windows
targetos: Windows
req.typenames: VHF_CONFIG, *PVHF_CONFIG
req.product: Windows 10 or later.
---

# _VHF_CONFIG structure
Contains initial configuration information that is provided by the HID source driver when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/dn925036">VhfCreate</a> to create a virtual HID device.

## Syntax
```
typedef struct _VHF_CONFIG {
  ULONG                               Size;
  PVOID                               VhfClientContext;
  ULONG                               OperationContextSize;
  PDEVICE_OBJECT                      DeviceObject;
  PVOID                               Reserved;
  USHORT                              VendorID;
  USHORT                              ProductID;
  USHORT                              VersionNumber;
  GUID                                ContainerID;
  USHORT                              InstanceIDLength;
  PWSTR                               InstanceID;
  USHORT                              ReportDescriptorLength;
  PUCHAR                              ReportDescriptor;
  PEVT_VHF_READY_FOR_NEXT_READ_REPORT EvtVhfReadyForNextReadReport;
  PEVT_VHF_ASYNC_OPERATION            EvtVhfAsyncOperationGetFeature;
  PEVT_VHF_ASYNC_OPERATION            EvtVhfAsyncOperationSetFeature;
  PEVT_VHF_ASYNC_OPERATION            EvtVhfAsyncOperationWriteReport;
  PEVT_VHF_ASYNC_OPERATION            EvtVhfAsyncOperationGetInputReport;
  PEVT_VHF_CLEANUP                    EvtVhfCleanup;
  USHORT                              HardwareIDsLength;
  PWSTR                               HardwareIDs;
} VHF_CONFIG, *PVHF_CONFIG;
```

## Members


`Size`

Required. Size of this structure initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/dn925046">VHF_CONFIG_INIT</a>.

`VhfClientContext`

Optional. An opaque pointer to HID source driver-allocated memory that the Virtual HID Framework (VHF) passes when it invokes  those callback functions.

`OperationContextSize`

Optional. Size of the buffer that VHF must allocate for an asynchronous operation started by <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a>. If non-zero, VHF allocates a buffer of this size and passes a pointer to that buffer in the <i>VhfOperationContext</i> parameter each time it invokes <i>EvtVhfAsyncOperation</i> to start a new operation.

`DeviceObject`

Required. A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure for the HID source driver. Get that pointer by calling  <a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a> and passing the WDFDEVICE handle that the driver received in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> call.

`Reserved`



`VendorID`

Optional. Vendor ID of the virtual HID device to be created.

`ProductID`

Optional. Product ID of the virtual HID device to be created.

`VersionNumber`

Optional. Version number of the virtual HID device to be created.

`ContainerID`

Optional. Container ID of the virtual HID device to be created.

`InstanceIDLength`



`InstanceID`



`ReportDescriptorLength`

Required. The length of the HID Report Descriptor contained in a buffer pointed by <b>ReportDescriptor</b>.

`ReportDescriptor`

Required. A pointer to a HID source driver-allocated buffer that contains the  HID Report Descriptor.

`EvtVhfReadyForNextReadReport`

Optional. A pointer to an <a href="https://msdn.microsoft.com/02DDBE00-C342-474B-8D06-FBB929BA4760">EvtVhfReadyForNextReadReport</a> callback. The HID source driver must implement and register this callback function if it wants to handle the buffering policy for submitting HID Input Reports. If this callback is specified, VHF does not buffer those reports. The HID source driver should submit one report by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn925040">VhfReadReportSubmit</a>, each time VHF invokes   <i>EvtVhfReadyForNextReadReport</i>.

`EvtVhfAsyncOperationGetFeature`

Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a get a HID Feature Report associated with a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">Top-Level Collection</a> from the HID class driver pair.
The driver can get a Feature Report only if the Report Descriptor declares it.

`EvtVhfAsyncOperationSetFeature`

Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a send  a HID Feature Report associated with a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">Top-Level Collection</a> to the HID class driver pair. The driver can set a Feature Report only if the Report Descriptor declares it.

`EvtVhfAsyncOperationWriteReport`

Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to a support HID Output Reports and send  them to the  HID class driver pair.

`EvtVhfAsyncOperationGetInputReport`

Optional. A pointer to an <a href="https://msdn.microsoft.com/C42174FE-202F-405D-840B-8613762F43AC">EvtVhfAsyncOperation</a> callback. The HID source driver must implement and register this callback function if it wants to support on-demand query for Input Reports.

`EvtVhfCleanup`

Optional. A pointer to a <a href="https://msdn.microsoft.com/1D477E7B-E4EA-46E7-872C-3BEBFBD31702">EvtVhfCleanup</a> callback. The HID source driver can implement and register this callback function if it wants to free the allocated resources for the virtual HID device.

`HardwareIDsLength`



`HardwareIDs`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | vhf.h |

## See Also

<a href="https://msdn.microsoft.com/26964963-792F-4529-B4FC-110BF5C65B35">Write a HID source driver by using Virtual HID Framework (VHF)</a>