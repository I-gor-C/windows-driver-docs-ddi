---
UID: NC:hwnclx.HWN_CLIENT_GET_STATE
title: HWN_CLIENT_GET_STATE
author: windows-driver-content
description: Implemented by the client driver to get hardware notification component state. It is invoked when a user requests status information.
old-location: gpiobtn\hwn_client_get_state.htm
old-project: gpiobtn
ms.assetid: c472b4bf-4c7f-4c30-ad03-2017d26d52b4
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PHWN_CLIENT_GET_STATE, *PHWN_CLIENT_GET_STATE callback function pointer, HWN_CLIENT_GET_STATE, HwnClientGetState, HwnClientGetState callback function, gpiobtn.hwn_client_get_state, hwnclx/HwnClientGetState"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	Hwnclx.h
api_name:
-	*PHWN_CLIENT_GET_STATE
product: Windows
targetos: Windows
req.typenames: HPMI_QUERY_CAPABILITIES_RESPONSE, *PHPMI_QUERY_CAPABILITIES_RESPONSE
---


# HWN_CLIENT_GET_STATE callback function
Implemented by the client driver to get hardware notification component state. It is invoked when a user requests status information.

## Syntax

```
HWN_CLIENT_GET_STATE HwnClientGetState;

NTSTATUS HwnClientGetState(
  PVOID Context,
  PVOID OutputBuffer,
  ULONG OutputBufferLength,
  PVOID InputBuffer,
  ULONG InputBufferLength,
  PULONG BytesRead
)
{...}
```

## Parameters

`Context`

Pointer to the client driver's context information. This memory space is available for use by the client driver. It is allocated as part of the framework object context space by <b>WdfDeviceCreate</b>. For more information, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_CLIENT_REGISTRATION_PACKET</a> and  <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space">Framework Object Context Space</a>.

`OutputBuffer`

Buffer of <i>OutputBufferLength</i> bytes for writing hardware notification status. If the function succeeds, the buffer will contain a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_HEADER</a> structure including one or more <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_SETTINGS</a> structures.

<div class="alert"><b>Note</b>  <p class="note"><b>OutputBufferLength</b> must be large enough to contain all of the requested settings. For more information, see Remarks.

</div>
<div> </div>

`OutputBufferLength`

The size of <i>OutputBuffer</i> in bytes.

`InputBuffer`

Buffer of <i>InputBufferLength</i> bytes containing a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_HEADER</a> holding one or more <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_SETTINGS</a> structures where the IDs for the requested hardware notification components are stored in the <b>HwNId</b> field. This buffer can be NULL.

`InputBufferLength`

The size of <i>InputBuffer</i> in bytes.

`BytesRead`

Pointer to a variable that indicates the number of bytes read by the function.


## Return Value

Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.

## Remarks

Register your implementation of this callback function by setting the appropriate member of <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_CLIENT_REGISTRATION_PACKET</a> and then calling <a href="..\hwnclx\nf-hwnclx-hwnregisterclient.md">HwNRegisterClient</a>.

<ul>
<li>
If <i>InputBuffer</i> is NULL, the output buffer will be used to store a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_HEADER</a> structure that contains all of the settings for the hardware notifications implemented by the driver. 

The Settings for a hardware notification component are stored in a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_SETTINGS</a> structure. The <b>HwNSettingsInfo</b> field of the <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_HEADER</a> structure contains an array of <b>HWN_SETTINGS</b> structures.

</li>
<li>
If <i>InputBuffer</i> is not null and is correctly formatted, it will contain a <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_HEADER</a> with one or more <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn/create-a-hardware-notification-client-driver">HWN_SETTINGS</a> structures. The IDs for the requested hardware notification components are stored in the <b>HwNId</b> field of the <b>HWN_SETTINGS</b> structure. The remaining settings should be valid settings or zero.

</li>
<li>
If <i>OutputBuffer</i> is not large enough to contain all of the settings requested, this function should not write anything to <i>OutputBuffer</i>. Additionally, it should set <i>BytesRead</i> to 0 and return an error.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | hwnclx.h |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a>



<a href="https://msdn.microsoft.com/405ff6db-9bc0-42f3-a740-49dd3967a8b3">Hardware notifications reference</a>