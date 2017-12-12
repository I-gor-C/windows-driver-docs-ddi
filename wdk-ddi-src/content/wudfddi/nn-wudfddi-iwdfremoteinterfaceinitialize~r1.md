---
UID: NN.wudfddi.IWDFRemoteInterfaceInitialize~r1
title: IWDFRemoteInterfaceInitialize
author: windows-driver-content
description: UMDF-based drivers receive the IWDFRemoteInterfaceInitialize interface as input to an IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival callback function.
old-location: wdf\iwdfremoteinterfaceinitialize.htm
old-project: wdf
ms.assetid: 54954874-d67a-4e8b-b791-105e8018f8ca
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFRemoteInterfaceInitialize
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
req.product: Windows 10 or later.
---

# IWDFRemoteInterfaceInitialize interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

UMDF-based drivers receive the <b>IWDFRemoteInterfaceInitialize</b> interface as input to an <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a> callback function.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFRemoteInterfaceInitialize</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IWDFRemoteInterfaceInitialize</b> also has these types of members:

The <b>IWDFRemoteInterfaceInitialize</b> interface has these methods.

The <a href="wdf.iwdfremoteinterfaceinitialize_getinterfaceguid">GetInterfaceGuid</a> method retrieves the GUID that identifies a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

The <a href="wdf.iwdfremoteinterfaceinitialize_retrievesymboliclink">RetrieveSymbolicLink</a> method retrieves the symbolic link name that the operating system assigned to a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

 


## -members
The <b>IWDFRemoteInterfaceInitialize</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremoteinterfaceinitialize_getinterfaceguid">IWDFRemoteInterfaceInitialize::GetInterfaceGuid</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremoteinterfaceinitialize_getinterfaceguid">GetInterfaceGuid</a> method retrieves the GUID that identifies a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremoteinterfaceinitialize_retrievesymboliclink">IWDFRemoteInterfaceInitialize::RetrieveSymbolicLink</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremoteinterfaceinitialize_retrievesymboliclink">RetrieveSymbolicLink</a> method retrieves the symbolic link name that the operating system assigned to a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

</td>
</tr>
</table>The <a href="wdf.iwdfremoteinterfaceinitialize_getinterfaceguid">GetInterfaceGuid</a> method retrieves the GUID that identifies a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

The <a href="wdf.iwdfremoteinterfaceinitialize_retrievesymboliclink">RetrieveSymbolicLink</a> method retrieves the symbolic link name that the operating system assigned to a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>. 

 


## -remarks


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
<dt>Wudfddi.h</dt>
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