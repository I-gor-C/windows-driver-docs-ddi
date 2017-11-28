---
UID: NF.wudfddi.IWDFDeviceInitialize.RetrieveDevicePropertyStore
title: IWDFDeviceInitialize::RetrieveDevicePropertyStore
author: windows-driver-content
description: The RetrieveDevicePropertyStore method retrieves a device property store that clients can read and write device properties through.
old-location: wdf\iwdfdeviceinitialize_retrievedevicepropertystore.htm
old-project: wdf
ms.assetid: 57d03610-b195-4691-8ee9-26c93560700c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDeviceInitialize, RetrieveDevicePropertyStore, IWDFDeviceInitialize::RetrieveDevicePropertyStore
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDeviceInitialize.RetrieveDevicePropertyStore
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDeviceInitialize
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize::RetrieveDevicePropertyStore method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a device property store that clients can read and write device properties through.</p>


## -syntax

````
HRESULT RetrieveDevicePropertyStore(
  [in, optional]  PCWSTR                            pcwszServiceName,
  [in]            WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,
  [out]           IWDFNamedPropertyStore            **ppPropStore,
  [out, optional] WDF_PROPERTY_STORE_DISPOSITION    *pDisposition
);
````


## -parameters
<dl>

### -param <i>pcwszServiceName</i> [in, optional]

<dd>
<p>A pointer to a <b>NULL</b>-terminated string that represents the name of the device property store. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not supply a name for a device property store. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561449">WDF_PROPERTY_STORE_RETRIEVE_FLAGS</a>-typed value that identifies how to retrieve the device property store. </p>
</dd>

### -param <i>ppPropStore</i> [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560164">IWDFNamedPropertyStore</a> interface that is used to retrieve device properties.</p>
</dd>

### -param <i>pDisposition</i> [out, optional]

<dd>
<p>A pointer to a variable that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561440">WDF_PROPERTY_STORE_DISPOSITION</a>-typed value that identifies whether the framework created the device property store or the device property store already existed. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require the disposition information. </p>
</dd>
</dl>

## -returns
<p>
<a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The caller should call the <b>Release</b> method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560164">IWDFNamedPropertyStore</a> interface after finishing with the property store. </p>

<p>For more information, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

<p>The caller should call the <b>Release</b> method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560164">IWDFNamedPropertyStore</a> interface after finishing with the property store. </p>

<p>For more information, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

## -requirements
<table>
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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556965">IWDFDeviceInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560164">IWDFNamedPropertyStore</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561440">WDF_PROPERTY_STORE_DISPOSITION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561449">WDF_PROPERTY_STORE_RETRIEVE_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDeviceInitialize::RetrieveDevicePropertyStore method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
