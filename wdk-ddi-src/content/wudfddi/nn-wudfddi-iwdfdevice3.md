---
UID: NN:wudfddi.IWDFDevice3
title: IWDFDevice3
author: windows-driver-content
description: To obtain the IWDFDevice3 interface, drivers call IWDFDevice::QueryInterface.
old-location: wdf\iwdfdevice3.htm
old-project: wdf
ms.assetid: C4AEC0DA-EB93-481D-A94C-7BB7BF15EFBC
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFDevice3, IWDFDevice3 interface, IWDFDevice3 interface, described, umdf.iwdfdevice3, wdf.iwdfdevice3, wudfddi/IWDFDevice3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
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
-	IWDFDevice3
product:
- Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFDevice3 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFDevice3</b> interface, drivers call <b>IWDFDevice::QueryInterface</b>.

## Methods

<p>The <b>IWDFDevice3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFDevice3::AssignS0IdleSettingsEx](nf-wudfddi-iwdfdevice3-assigns0idlesettingsex.md) | The AssignS0IdleSettingsEx method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [IWDFDevice3::CreateInterrupt](nf-wudfddi-iwdfdevice3-createinterrupt.md) | The CreateInterrupt method creates a framework interrupt object. |
| [IWDFDevice3::CreateWorkItem](nf-wudfddi-iwdfdevice3-createworkitem.md) | The CreateWorkItem method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue. |
| [IWDFDevice3::GetHardwareRegisterMappedAddress](nf-wudfddi-iwdfdevice3-gethardwareregistermappedaddress.md) | A driver calls GetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it earlier mapped using MapIoSpace. |
| [IWDFDevice3::MapIoSpace](nf-wudfddi-iwdfdevice3-mapiospace.md) | The MapIoSpace method maps the given physical address range to system address space and returns a pseudo base address. |
| [IWDFDevice3::ReadFromHardware](nf-wudfddi-iwdfdevice3-readfromhardware.md) | The ReadFromHardware method is used internally by the framework. Do not use. |
| [IWDFDevice3::UnmapIoSpace](nf-wudfddi-iwdfdevice3-unmapiospace.md) | The UnmapIoSpace method unmaps a specified range of physical addresses previously mapped by MapIoSpace method. |
| [IWDFDevice3::WriteToHardware](nf-wudfddi-iwdfdevice3-writetohardware.md) | The WriteToHardware method is used internally by the framework. Do not use. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a>