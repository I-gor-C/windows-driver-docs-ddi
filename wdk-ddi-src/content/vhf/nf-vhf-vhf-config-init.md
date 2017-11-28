---
UID: NF.vhf.VHF_CONFIG_INIT
title: VHF_CONFIG_INIT
author: windows-driver-content
description: Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver.
old-location: hid\vhf_config_init.htm
old-project: hid
ms.assetid: 4A87D9E2-F1FC-4CA8-834C-E545D8F0277B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: VHF_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: vhf.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VHF_CONFIG_INIT
req.alt-loc: vhfKm.lib,vhfKm.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: VhfKm.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# VHF_CONFIG_INIT function



## -description
<p>Use the <b>VHF_CONFIG_INIT</b> function to initialize the required members of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925044">VHF_CONFIG</a> structure allocated by the HID source driver.</p>


## -syntax

````
FORCEINLINE void VHF_CONFIG_INIT(
  _Out_ PVHF_CONFIG                                     Config,
  _In_  PDEVICE_OBJECT                                  DeviceObject,
  _In_  USHORT                                          ReportDescriptorLength,
        _In_reads_bytes_(ReportDescriptorLength) PUCHAR ReportDescriptor
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/dn925044">VHF_CONFIG</a> structure to initialize.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> structure for the HID source driver. Get that pointer by calling  <a href="https://msdn.microsoft.com/library/windows/hardware/ff546942">WdfDeviceWdmGetDeviceObject</a> and passing the WDFDEVICE handle that the driver received in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> call. </p>
</dd>

### -param <i>ReportDescriptorLength</i> [in]

<dd>
<p>The length of the HID Report Descriptor contained in a buffer pointer by <i>ReportDescriptor</i>.</p>
</dd>

### -param <i>ReportDescriptor</i> 

<dd>
<p>A pointer to a HID source driver-allocated buffer that contains the  HID Report Descriptor.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>VhfKm.lib</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20VHF_CONFIG_INIT function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
