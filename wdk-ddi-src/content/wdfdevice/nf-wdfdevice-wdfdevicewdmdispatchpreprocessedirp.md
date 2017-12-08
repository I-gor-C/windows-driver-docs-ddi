---
UID: NF.wdfdevice.WdfDeviceWdmDispatchPreprocessedIrp
title: WdfDeviceWdmDispatchPreprocessedIrp function
author: windows-driver-content
description: The WdfDeviceWdmDispatchPreprocessedIrp method returns a preprocessed IRP to the framework.
old-location: wdf\wdfdevicewdmdispatchpreprocessedirp.htm
old-project: wdf
ms.assetid: 83b18680-0b58-4278-87ff-757eb6e76178
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceWdmDispatchPreprocessedIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceWdmDispatchPreprocessedIrp
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceWdmDispatchPreprocessedIrp function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfDeviceWdmDispatchPreprocessedIrp</b> method returns a  preprocessed IRP to the framework.


## -syntax

````
NTSTATUS WdfDeviceWdmDispatchPreprocessedIrp(
  _In_ WDFDEVICE Device,
  _In_ PIRP      Irp
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.

### -param Irp [in]

A pointer to an <a href="kernel.irp">IRP</a> structure.

## -returns
<b>WdfDeviceWdmDispatchPreprocessedIrp</b> returns an NTSTATUS value that that framework or the driver provides as the result of processing the IRP. The driver must use this return value as the return value for the <a href="..\wdfdevice\nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function.

A bug check occurs if the driver supplies an invalid object handle.

## -remarks
A framework-based driver that preprocesses or postprocesses WDM IRPs must call <b>WdfDeviceWdmDispatchPreprocessedIrp</b>, typically from within the driver's <a href="..\wdfdevice\nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess.md">EvtDeviceWdmIrpPreprocess</a> callback function. For more information about how to call <b>WdfDeviceWdmDispatchPreprocessedIrp</b>, see <a href="wdf.preprocessing_and_postprocessing_irps">Preprocessing and Postprocessing IRPs</a>.

For a code example that uses <b>WdfDeviceWdmDispatchPreprocessedIrp</b>, see <a href="wdf.preprocessing_and_postprocessing_irps">Preprocessing and Postprocessing IRPs</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>