---
UID: NF.wudfddi.IWDFRemoteTarget.OpenRemoteInterface
title: IWDFRemoteTarget::OpenRemoteInterface method
author: windows-driver-content
description: The OpenRemoteInterface method opens a device interface so that the driver can send I/O requests to it.
old-location: wdf\iwdfremotetarget_openremoteinterface.htm
old-project: wdf
ms.assetid: 5d278cde-3ebe-4fee-86fd-1ec4e79bd837
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFRemoteTarget, IWDFRemoteTarget::OpenRemoteInterface, OpenRemoteInterface
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
req.alt-api: IWDFRemoteTarget.OpenRemoteInterface
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

# IWDFRemoteTarget::OpenRemoteInterface method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>OpenRemoteInterface</b> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.



## -syntax

````
HRESULT OpenRemoteInterface(
  [in]           IWDFRemoteInterface         *pRemoteInterface,
  [in, optional] PCWSTR                      pszRelativeFileName,
  [in]           DWORD                       DesiredAccess,
  [in, optional] PUMDF_IO_TARGET_OPEN_PARAMS pOpenParams
);
````


## -parameters

### -param pRemoteInterface [in]

A pointer to a <a href="..\wudfddi\nn-wudfddi-iwdfremoteinterface.md">IWDFRemoteInterface</a> interface that the driver obtained from a previous call to <a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a>.


### -param pszRelativeFileName [in, optional]

An optional pointer to a caller-supplied, <b>null</b>-terminated string that the framework appends to the symbolic link name of the device interface. 


### -param DesiredAccess [in]

A bitmask that specifies the caller's desired access to the file. For more information about this member, see the <i>DesiredAccess</i> parameter of <a href="http://go.microsoft.com/fwlink/p/?linkid=152795">CreateFile</a> in the Windows SDK.


### -param pOpenParams [in, optional]

A pointer to a caller-allocated <a href="wdf.umdf_io_target_open_params">UMDF_IO_TARGET_OPEN_PARAMS</a> structure that contains additional parameters. This parameter is optional and can be <b>NULL</b>.


## -returns
<b>OpenRemoteInterface</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following value:
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>The framework's attempt to allocate memory failed. 

 

This method might return one of the other values that Winerror.h contains.



The framework's <a href="wdf.using_umdf_verifier">verifier</a> reports an error if the framework cannot open the file.


## -remarks
After a driver's <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function receives notification that a device interface is available, and after the driver calls <a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a> to create a remote interface object, the driver can call <b>OpenRemoteInterface</b> so that it can send I/O requests to the device interface.

The device interface must be accessible by the account that loaded the UMDF-based driver, which is typically the Local Service account. However, if the driver uses <a href="wdf.handling_client_impersonation">impersonation</a> when it calls <b>OpenRemoteInterface</b>, the device interface must be accessible by the impersonated account.

For more information about <b>OpenRemoteInterface</b> and how to use device interfaces in UMDF-based drivers, see <a href="wdf.using_device_interfaces_in_umdf_drivers">Using Device Interfaces in UMDF-based Drivers</a>.

The following code example shows how an <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function can create a remote interface and remote target objects for a device interface and then open the interface for I/O operations.


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
<a href="..\wudfddi\nn-wudfddi-iwdfremotetarget.md">IWDFRemoteTarget</a>
</dt>
<dt>
<a href="wdf.iwdfremotetarget_openfilebyname">IWDFRemoteTarget::OpenFileByName</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFRemoteTarget::OpenRemoteInterface method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

