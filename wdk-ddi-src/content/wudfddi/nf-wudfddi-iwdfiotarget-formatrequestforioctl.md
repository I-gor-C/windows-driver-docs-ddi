---
UID: NF:wudfddi.IWDFIoTarget.FormatRequestForIoctl
title: IWDFIoTarget::FormatRequestForIoctl method
author: windows-driver-content
description: The FormatRequestForIoctl method formats an I/O request object for an I/O control operation.
old-location: wdf\iwdfiotarget_formatrequestforioctl.htm
old-project: wdf
ms.assetid: fd0bbd6e-bb23-4d0c-9cac-9bb7657876a0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: FormatRequestForIoctl method, FormatRequestForIoctl method, IWDFIoTarget interface, FormatRequestForIoctl,IWDFIoTarget.FormatRequestForIoctl, IWDFIoTarget, IWDFIoTarget interface, FormatRequestForIoctl method, IWDFIoTarget::FormatRequestForIoctl, UMDFIoTargetObjectRef_9c72ba41-4a3f-4bea-8ca1-bcf04dd033ad.xml, umdf.iwdfiotarget_formatrequestforioctl, wdf.iwdfiotarget_formatrequestforioctl, wudfddi/IWDFIoTarget::FormatRequestForIoctl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFIoTarget.FormatRequestForIoctl
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---


# IWDFIoTarget::FormatRequestForIoctl method
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>FormatRequestForIoctl</b> method formats an I/O request object for an I/O control operation.

## Syntax

```
HRESULT FormatRequestForIoctl(
  IWDFIoRequest     *pRequest,
  ULONG             IoctlCode,
  IWDFFile          *pFile,
  IWDFMemory        *pInputMemory,
  PWDFMEMORY_OFFSET pInputMemoryOffset,
  IWDFMemory        *pOutputMemory,
  PWDFMEMORY_OFFSET pOutputMemoryOffset
);
```

## Parameters

`pRequest`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a> interface for the request object to format.

`IoctlCode`

A control code that identifies a specific operation to perform.

`pFile`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface for the file object that is associated with the I/O control request. For the default I/O target, this parameter must be non-NULL.

`pInputMemory`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface that is used to access the input buffer for the request. This parameter is optional.

`pInputMemoryOffset`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a> structure that describes the input memory offset for the request. This parameter is optional.

`pOutputMemory`

A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface that is used to access the output buffer for the request. This parameter is optional.

`pOutputMemoryOffset`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a> structure that describes the output memory offset for the request. This parameter is optional.


## Return Value

<b>FormatRequestForIoctl</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |
| **DLL** | WUDFx.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a>