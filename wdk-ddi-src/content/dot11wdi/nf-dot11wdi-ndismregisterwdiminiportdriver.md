---
UID: NF.dot11wdi.NdisMRegisterWdiMiniportDriver
title: NdisMRegisterWdiMiniportDriver
author: windows-driver-content
description: A miniport driver calls the NdisMRegisterWdiMiniportDriver function to register MiniportWdiXxx entry points with NDIS as the first step in initialization.
old-location: netvista\ndismregisterwdiminiportdriver.htm
old-project: netvista
ms.assetid: 60FE4E6C-38D4-438F-983B-7336926F6FE2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMRegisterWdiMiniportDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMRegisterWdiMiniportDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisMRegisterWdiMiniportDriver function



## -description
<p>A miniport driver calls the NdisMRegisterWdiMiniportDriver function to register MiniportWdiXxx entry points with NDIS as the first step in initialization.</p>


## -syntax

````
NDIS_STATUS NdisMRegisterWdiMiniportDriver(
  _In_     DRIVER_OBJECT                            *DriverObject,
  _In_     PCUNICODE_STRING                         RegistryPath,
  _In_opt_ NDIS_MINIPORT_DRIVER_CONTEXT             NdisDriverContext,
  _In_     NDIS_MINIPORT_DRIVER_CHARACTERISTICS     *MiniportDriverCharacteristics,
  _In_     NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS *MiniportWdiCharacteristics,
  _Out_    NDIS_MINIPORT_DRIVER_HANDLE              *NdisMiniportDriverHandle
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to an opaque driver object that the miniport driver received in its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine at the 
     <i>Argument1</i> parameter (see 
     <a href="netvista.driverentry_of_ndis_miniport_drivers">DriverEntry of NDIS
     Miniport Drivers</a>).</p>
</dd>

### -param <i>RegistryPath</i> [in]

<dd>
<p>A pointer to an opaque registry path that the miniport driver received in its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine at the 
     <i>Argument2</i> parameter.</p>
</dd>

### -param <i>NdisDriverContext</i> [in, optional]

<dd>
<p>A handle to a driver-allocated context area where the driver maintains state and configuration
     information.</p>
</dd>

### -param <i>MiniportDriverCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-miniport-driver-characteristics.md">
     NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a> structure that the caller initialized.</p>
</dd>

### -param <i>MiniportWdiCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     
     <a href="https://msdn.microsoft.com/library/windows/hardware/mt297617">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a> structure that the caller initialized.</p>
</dd>

### -param <i>NdisMiniportDriverHandle</i> [out]

<dd>
<p>A pointer to a caller-supplied handle variable. NDIS writes a handle to this variable that
     uniquely identifies this driver. The driver must save this handle for use in subsequent 
     <b>Ndis<i>Xxx</i></b> function calls.</p>
</dd>
</dl>

## -returns
<p>
            NdisMRegisterWdiMiniportDriver can return any of the following return values.</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NdisMRegisterWdiMiniportDriver registered the WDI miniport driver successfully.</p><dl>
<dt><b>NDIS_STATUS_BAD_CHARACTERISTICS</b></dt>
</dl><p>The 
       <i>CharacteristicsLength</i> parameter is incorrect for the NDIS version that is specified at the 
       <b>MajorNdisVersion</b> member in the structure at 
       <i>MiniportDriverCharacteristics</i> .</p><dl>
<dt><b>NDIS_STATUS_BAD_VERSION</b></dt>
</dl><p>The 
       <b>MajorNdisVersion</b> or 
       <b>MinorNdisVersion</b> specified in the characteristics structure is invalid.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>A shortage of resources, possibly memory, prevented NDIS from registering the caller.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>This is a default error status, returned when none of the preceding errors caused the
       registration to fail.</p><dl>
<dt><b>Other NDIS_STATUS codes</b></dt>
</dl><p>An appropriate NDIS_STATUS code in the case of a failure.</p>

<p> </p>

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
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565958">NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt297617">NDIS_MINIPORT_DRIVER_WDI_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterWdiMiniportDriver function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
