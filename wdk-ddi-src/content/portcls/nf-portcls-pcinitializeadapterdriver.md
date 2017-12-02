---
UID: NF.portcls.PcInitializeAdapterDriver
title: PcInitializeAdapterDriver
author: windows-driver-content
description: The PcInitializeAdapterDriver function binds an adapter driver to the PortCls system driver.
old-location: audio\pcinitializeadapterdriver.htm
old-project: audio
ms.assetid: c9d019da-a05b-4c60-99e9-06b8537fa78e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcInitializeAdapterDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcInitializeAdapterDriver function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcInitializeAdapterDriver
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcInitializeAdapterDriver function



## -description
<p>The <b>PcInitializeAdapterDriver</b> function binds an adapter driver to the PortCls system driver. IRP handlers and handlers for device addition and removal are installed in the driver object. Adapter drivers that need to bind to more than one class driver should not call this function.</p>


## -syntax

````
NTSTATUS PcInitializeAdapterDriver(
  _In_ PDRIVER_OBJECT     DriverObject,
  _In_ PUNICODE_STRING    RegistryPathName,
  _In_ PDRIVER_ADD_DEVICE AddDevice
);
````


## -parameters
<dl>

### -param DriverObject [in]

<dd>
<p>Pointer to the driver object, which is a system structure of type <a href="..\wdm\ns-wdm--driver-object.md">DRIVER_OBJECT</a>. This pointer is passed as a parameter to the adapter's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> function.</p>
</dd>

### -param RegistryPathName [in]

<dd>
<p>Specifies the registry path name that is to be passed as a parameter to the adapter's <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> function.</p>
</dd>

### -param AddDevice [in]

<dd>
<p>Pointer to the adapter's <a href="kernel.adddevice">AddDevice</a> function. This is a pointer of type PDRIVER_ADD_DEVICE, which is defined in ntddk.h to be:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>  NTSTATUS
    (*PDRIVER_ADD_DEVICE)(
      IN struct _DRIVER_OBJECT  *DriverObject,
      IN struct _DEVICE_OBJECT  *PhysicalDeviceObject
        );</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>

## -returns
<p><b>PcInitializeAdapterDriver</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>The <a href="kernel.adddevice">AddDevice</a> handler supplied in the call to this function should call <a href="..\portcls\nf-portcls-pcaddadapterdevice.md">PcAddAdapterDevice</a>. For more information, see <a href="https://msdn.microsoft.com/bf88b9de-f4c4-4f9c-9355-603789b9ad3d">Startup Sequence</a>.</p>

<p>The <b>PcInitializeAdapterDriver</b> function loads pointers to handlers for the following IRPs into the driver object:</p>

<p>IRP_MJ_CLOSE</p>

<p>IRP_MJ_CREATE</p>

<p>IRP_MJ_DEVICE_CONTROL</p>

<p>IRP_MJ_FLUSH_BUFFERS</p>

<p>IRP_MJ_PNP</p>

<p>IRP_MJ_POWER</p>

<p>IRP_MJ_QUERY_SECURITY</p>

<p>IRP_MJ_READ</p>

<p>IRP_MJ_SET_SECURITY</p>

<p>IRP_MJ_SYSTEM_CONTROL</p>

<p>IRP_MJ_WRITE</p>

<p>PortCls uses its own internal handlers for the CREATE, PNP, POWER, and SYSTEM_CONTROL IRPs above. It uses the default KS handlers for the other seven IRPs.</p>

<p>An adapter driver that overwrites one or more of the pointers above with a pointer to its own IRP handler can call <a href="..\portcls\nf-portcls-pcdispatchirp.md">PcDispatchIrp</a> from within its handler routine in order to forward the IRP to PortCls. For a code example, see the SB16 sample audio driver in the Microsoft Windows Driver Kit (WDK).</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcInitializeAdapterDriver function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="..\wdm\ns-wdm--driver-object.md">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a>
</dt>
<dt>
<a href="kernel.adddevice">AddDevice</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcaddadapterdevice.md">PcAddAdapterDevice</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcdispatchirp.md">PcDispatchIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcInitializeAdapterDriver function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
