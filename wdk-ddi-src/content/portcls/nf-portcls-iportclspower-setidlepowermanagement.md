---
UID: NF.portcls.IPortClsPower.SetIdlePowerManagement
title: IPortClsPower::SetIdlePowerManagement
author: windows-driver-content
description: The SetIdlePowerManagement method provides a way for the adapter driver to opt in or opt out of idle state detection.
old-location: audio\iportclspower_setidlepowermanagement.htm
old-project: audio
ms.assetid: ccef350c-7c46-43fa-8834-b0d712d9cf38
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortClsPower, SetIdlePowerManagement, IPortClsPower::SetIdlePowerManagement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsPower.SetIdlePowerManagement
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: IPortClsPower
---

# IPortClsPower::SetIdlePowerManagement method



## -description
<p>The <code>SetIdlePowerManagement</code> method provides a way for the adapter driver to opt in or opt out of idle state detection.</p>


## -syntax

````
NTSTATUS SetIdlePowerManagement(
  [in] PDEVICE_OBJECT DeviceObject,
  [in] BOOLEAN        bEnabled
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>Specifies a pointer to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> structure that represents the functional device object of the adapter.</p>
</dd>

### -param bEnabled [in]

<dd>
<p>Specifies a Boolean variable that indicates whether idle state detection is enabled or disabled.</p>
</dd>
</dl>

## -returns
<p>The <code>SetIdlePowerManagement</code> method returns STATUS_SUCCESS if the call was successful. Otherwise, it returns the appropriate error code. </p>

## -remarks
<p>When the <i>bEnabled</i> parameter is set to <b>TRUE</b>, it indicates that the adapter driver has enabled idle state detection. When the system determines that the adapter is idle, the adapter can be put into the sleep state to save power. If the adapter was not designed to suppress the popping sound that is normally associated with power-up, it is possible that the adapter can experience a popping effect when it comes out of the sleep state.</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iportclspower.md">IPortClsPower</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/43721EC9-4901-4C68-9CCC-E0A71BF2200E">Immediate Idle Timeout Opt-in</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortClsPower::SetIdlePowerManagement method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
