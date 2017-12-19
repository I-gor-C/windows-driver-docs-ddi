---
UID: NF.wudfddi.IWDFDevice2.CreateRemoteInterface
title: IWDFDevice2::CreateRemoteInterface method
author: windows-driver-content
description: The CreateRemoteInterface method creates a remote interface object that represents a device interface.
old-location: wdf\iwdfdevice2_createremoteinterface.htm
old-project: wdf
ms.assetid: fb2def4b-c027-465d-b734-20b4b83a6308
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFDevice2, IWDFDevice2::CreateRemoteInterface, CreateRemoteInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2.CreateRemoteInterface
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFDevice2::CreateRemoteInterface method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>CreateRemoteInterface</b> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.



## -syntax

````
HRESULT CreateRemoteInterface(
  [in]           IWDFRemoteInterfaceInitialize *pRemoteInterfaceInit,
  [in, optional] IUnknown                      *pCallbackInterface,
  [out]          IWDFRemoteInterface           **ppRemoteInterface
);
````


## -parameters

### -param pRemoteInterfaceInit [in]

A pointer to an <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize.md">IWDFRemoteInterfaceInitialize</a> interface that the driver's <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function received.


### -param pCallbackInterface [in, optional]

A pointer to an optional, driver-supplied callback interface. The <b>IUnknown::QueryInterface</b> method of this interface must return a pointer to the driver's <a href="..\wudfddi\nn-wudfddi-iremoteinterfacecallbackevent.md">IRemoteInterfaceCallbackEvent</a> and <a href="..\wudfddi\nn-wudfddi-iremoteinterfacecallbackremoval.md">IRemoteInterfaceCallbackRemoval</a> interfaces, if the driver supports those interfaces. This parameter is optional and can be <b>NULL</b>.


### -param ppRemoteInterface [out]

A pointer to a driver-supplied location that receives a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterface.md">IWDFRemoteInterface</a> interface of the new remote interface object.


## -returns
<b>CreateRemoteInterface</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>The framework's attempt to allocate memory failed.

 

This method might return one of the other values that Winerror.h contains.


## -remarks
If your driver calls <b>CreateRemoteInterface</b>, it must do so from within its <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function.

For more information about <b>CreateRemoteInterface</b> and using device interfaces, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>


The following code example shows an <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function that creates a remote interface object, creates a remote target object, and opens the remote target for I/O operations.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a>
</dt>
<dt>
<a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a>
</dt>
<dt>
<a href="wdf.iwdfremotetarget_openremoteinterface">IWDFRemoteTarget::OpenRemoteInterface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::CreateRemoteInterface method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

