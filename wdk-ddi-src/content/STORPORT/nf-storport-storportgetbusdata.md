---
UID: NF.storport.StorPortGetBusData
title: StorPortGetBusData
author: windows-driver-content
description: The StorPortGetBusData routine retrieves the bus-specific configuration information necessary to initialize the HBA.
old-location: storage\storportgetbusdata.htm
ms.assetid: 19999e21-1afd-42ac-9809-b8ed4b6ac7e3
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetBusData
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
ms.keywords: StorPortGetBusData
req.iface: 
req.product: Windows 10 or later.
---

# StorPortGetBusData function



## -description
<p>The <b>StorPortGetBusData</b> routine retrieves the bus-specific configuration information necessary to initialize the HBA.</p>


## -syntax

````
ULONG StorPortGetBusData(
  _In_    PVOID DeviceExtension,
  _In_    ULONG BusDataType,
  _In_    ULONG SystemIoBusNumber,
  _In_    ULONG SlotNumber,
  _Inout_ PVOID Buffer,
  _In_    ULONG Length
);
````


## -parameters
<dl>

### -param <i>DeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's per-HBA storage area.</p>
</dd>

### -param <i>BusDataType</i> [in]

<dd>
<p>Contains a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff540700">BUS_DATA_TYPE</a> that specifies the type of bus-specific configuration data to be returned. Currently, this value can be one of the following: <b>Cmos</b>, <b>EisaConfiguration</b>, <b>Pos</b>, or <b>PCIConfiguration</b>. However, additional types of bus configuration will be supported in the future. The upper bound on the types supported is always <b>MaximumBusDataType</b>.</p>
</dd>

### -param <i>SystemIoBusNumber</i> [in]

<dd>
<p>Specifies the system-assigned number of the I/O bus. The miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine obtains this value from the <b>SystemIoBusNumber</b> member initially set in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>.</p>
</dd>

### -param <i>SlotNumber</i> [in]

<dd>
<p>Specifies the logical slot number or location of the device.</p>
<p>If <b>PCIConfiguration</b> is specified as the <i>BusDataType</i>, this parameter must be specified as a PCI_SLOT_NUMBER-type value.</p>
</dd>

### -param <i>Buffer</i> [in, out]

<dd>
<p>Pointer to a buffer or area to which the configuration data is returned or, if the given <i>Length</i> is zero, points to a location to which the OS-specific port driver returns a pointer to a buffer that it allocates.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the maximum number of bytes to return at <i>Buffer</i>, or zero if the caller requires the OS-specific port driver to allocate a buffer to contain the data.</p>
</dd>
</dl>

## -returns
<p><b>StorPortGetBusData</b> returns the number of bytes of configuration information it stored in the buffer. When the input <i>BusDataType</i> is <b>PCIConfiguration</b>, <b>StorPortGetBusData</b> can return either of the following values to indicate an error.</p><dl>
<dt><b>0 (zero)</b></dt>
</dl><p>The PCI bus does not exist.</p><dl>
<dt><b>2</b></dt>
</dl><p>The PCI bus exists, but there is no device at the given PCI <i>SlotNumber</i>. The <i>Buffer</i> contains the value PCI_INVALID_VENDOR_ID at the PCI_COMMON_CONFIG <b>VendorId</b> member.</p>

<p> </p>

## -remarks
<p><b>StorPortGetBusData</b> can be called only from a miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine or from <a href="https://msdn.microsoft.com/library/windows/hardware/ff557365">HwStorAdapterControl</a> when the control type is <b>ScsiSetRunningConfig</b>. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.</p>

<p>Configuration data returned by <b>StorPortGetBusData</b> is valid only until the miniport driver calls <b>StorPortGetBusData</b> again. As soon as the caller's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine returns control, any returned configuration data becomes invalid.</p>

<p><b>StorPortGetBusData</b> can be called only from a miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine or from <a href="https://msdn.microsoft.com/library/windows/hardware/ff557365">HwStorAdapterControl</a> when the control type is <b>ScsiSetRunningConfig</b>. Calls from other miniport driver routines will result in system failure or incorrect operation for the caller.</p>

<p>Configuration data returned by <b>StorPortGetBusData</b> is valid only until the miniport driver calls <b>StorPortGetBusData</b> again. As soon as the caller's <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a> routine returns control, any returned configuration data becomes invalid.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557390">HwStorFindAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortGetBusData routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
