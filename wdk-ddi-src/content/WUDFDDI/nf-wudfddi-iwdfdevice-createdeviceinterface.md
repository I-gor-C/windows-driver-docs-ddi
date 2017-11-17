---
UID: NF.wudfddi.IWDFDevice.CreateDeviceInterface
title: IWDFDevice::CreateDeviceInterface
author: windows-driver-content
description: The CreateDeviceInterface method creates an instance of a device interface class.
old-location: wdf\iwdfdevice_createdeviceinterface.htm
ms.assetid: 0a88cbb6-66be-4ef7-93da-27d7ce169779
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.CreateDeviceInterface
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
ms.keywords: IWDFDevice, CreateDeviceInterface, IWDFDevice::CreateDeviceInterface
req.iface: IWDFDevice
req.product: Windows 10 or later.
---

# IWDFDevice::CreateDeviceInterface method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateDeviceInterface</b> method creates an instance of a device interface class.</p>


## -syntax

````
HRESULT CreateDeviceInterface(
  [in]           LPCGUID pDeviceInterfaceGuid,
  [in, optional] PCWSTR  pReferenceString
);
````


## -parameters
<dl>

### -param <i>pDeviceInterfaceGuid</i> [in]

<dd>
<p>A pointer to the GUID for a device interface class.</p>
</dd>

### -param <i>pReferenceString</i> [in, optional]

<dd>
<p>A pointer to a <b>NULL</b>-terminated string that contains the name of the instance of the device interface. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not have to supply a name. If the driver must supply a name, the string that the driver passes must not contain any path separator characters ("/" or "\"). </p>
</dd>
</dl>

## -returns
<p><b>CreateDeviceInterface</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Drivers can use the <i>pReferenceString</i> parameter to differentiate different instances of a single interface. In other words, if a driver calls <b>CreateDeviceInterface</b> twice for the same device interface class, the driver can specify a different string for <i>pReferenceString</i> each time. When an instance of an interface is opened, the framework passes the instance's reference string to the driver. The reference string is appended to the path component of the interface instance's name. The driver can then use the reference string to determine which instance of the device interface class is being opened.</p>

<p>If <b>CreateDeviceInterface</b> succeeds, the initial state of the interface is disabled. If creation succeeds, the framework automatically enables and disables the interface based on the device's PnP state.  In addition, a driver can disable and re-enable a device interface as necessary by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a>.</p>

<p>For more information about device interfaces, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

<p>The following code example shows how to create a device interface instance. In this example, the driver explicitly calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a> to enable the interface.</p>

<p>Drivers can use the <i>pReferenceString</i> parameter to differentiate different instances of a single interface. In other words, if a driver calls <b>CreateDeviceInterface</b> twice for the same device interface class, the driver can specify a different string for <i>pReferenceString</i> each time. When an instance of an interface is opened, the framework passes the instance's reference string to the driver. The reference string is appended to the path component of the interface instance's name. The driver can then use the reference string to determine which instance of the device interface class is being opened.</p>

<p>If <b>CreateDeviceInterface</b> succeeds, the initial state of the interface is disabled. If creation succeeds, the framework automatically enables and disables the interface based on the device's PnP state.  In addition, a driver can disable and re-enable a device interface as necessary by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a>.</p>

<p>For more information about device interfaces, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.</p>

<p>The following code example shows how to create a device interface instance. In this example, the driver explicitly calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a> to enable the interface.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::CreateDeviceInterface method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
