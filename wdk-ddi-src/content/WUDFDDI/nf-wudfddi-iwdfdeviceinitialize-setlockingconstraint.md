---
UID: NF.wudfddi.IWDFDeviceInitialize.SetLockingConstraint
title: IWDFDeviceInitialize::SetLockingConstraint
author: windows-driver-content
description: The SetLockingConstraint method sets the synchronization (or locking) model for callback functions into the driver.
old-location: wdf\iwdfdeviceinitialize_setlockingconstraint.htm
ms.assetid: c0062ad4-6666-49db-9d53-70f2ed2353d1
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
req.alt-api: IWDFDeviceInitialize.SetLockingConstraint
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
ms.keywords: IWDFDeviceInitialize, SetLockingConstraint, IWDFDeviceInitialize::SetLockingConstraint
req.iface: IWDFDeviceInitialize
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize::SetLockingConstraint method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SetLockingConstraint</b> method sets the synchronization (or locking) model for callback functions into the driver.</p>


## -syntax

````
void SetLockingConstraint(
  [in] WDF_CALLBACK_CONSTRAINT LockType
);
````


## -parameters
<dl>

### -param <i>LockType</i> [in]

<dd>
<p>A value of type <a href="https://msdn.microsoft.com/118a9dcc-8dd4-454a-bab2-1558821781a7">WDF_CALLBACK_CONSTRAINT</a> that identifies the locking model.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>The default value of the <i>LockType</i> parameter is <b>WdfDeviceLevel</b>, which is currently the only supported value.</p>

<p>For a code example of how to use the <b>SetLockingConstraint</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a>.</p>

<p>The default value of the <i>LockType</i> parameter is <b>WdfDeviceLevel</b>, which is currently the only supported value.</p>

<p>For a code example of how to use the <b>SetLockingConstraint</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDeviceInitialize::SetLockingConstraint method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
