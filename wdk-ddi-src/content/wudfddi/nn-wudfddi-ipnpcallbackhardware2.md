---
UID : NN:wudfddi.IPnpCallbackHardware2
title : IPnpCallbackHardware2
author : windows-driver-content
description : The IPnpCallbackHardware2 interface exposes callback methods related to hardware.
old-location : wdf\ipnpcallbackhardware2.htm
old-project : wdf
ms.assetid : C0DB967F-0A1A-4749-B902-EBA0D59A3E45
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.ipnpcallbackhardware2, IPnpCallbackHardware2 interface, IPnpCallbackHardware2 interface, described, IPnpCallbackHardware2, wudfddi/IPnpCallbackHardware2, umdf.ipnpcallbackhardware2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.11
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : POWER_ACTION, *PPOWER_ACTION
req.product : Windows 10 or later.
---

# IPnpCallbackHardware2 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

  The <b>IPnpCallbackHardware2</b>  interface exposes callback methods related to hardware.

## Methods

<p>The <b>IPnpCallbackHardware2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IPnpCallbackHardware2.OnPrepareHardware](nf-wudfddi-ipnpcallbackhardware2-onpreparehardware.md) | The OnPrepareHardware method performs any operations that are needed to make a device accessible to the driver. |
| [wudfddi.IPnpCallbackHardware2.OnReleaseHardware](nf-wudfddi-ipnpcallbackhardware2-onreleasehardware.md) | The OnReleaseHardware method performs operations that are needed when a device is no longer accessible. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332">IUnknown</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardware2 interface%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>