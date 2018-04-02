---
UID: NN:wudfddi.IWDFInterrupt
title: IWDFInterrupt
author: windows-driver-content
description: This interface exposes an interrupt object.
old-location: wdf\iwdfinterrupt.htm
old-project: wdf
ms.assetid: 729A2361-6FE1-4096-AC8B-3D042326EE5C
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFInterrupt, IWDFInterrupt interface, IWDFInterrupt interface, described, umdf.iwdfinterrupt, wdf.iwdfinterrupt, wudfddi/IWDFInterrupt
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
-	IWDFInterrupt
product:
- Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFInterrupt interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

This interface exposes an interrupt object.

## Methods

<p>The <b>IWDFInterrupt</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFInterrupt::AcquireInterruptLock](nf-wudfddi-iwdfinterrupt-acquireinterruptlock.md) | The AcquireInterruptLock method begins a code sequence that executes while holding an interrupt object's lock. |
| [IWDFInterrupt::Disable](nf-wudfddi-iwdfinterrupt-disable.md) | The Disable method disables a specified device interrupt by calling the driver's OnInterruptDisable callback function. |
| [IWDFInterrupt::Enable](nf-wudfddi-iwdfinterrupt-enable.md) | The Enable method enables a specified device interrupt by calling the driver's OnInterruptEnable callback function. |
| [IWDFInterrupt::GetDevice](nf-wudfddi-iwdfinterrupt-getdevice.md) | The GetDevice method returns the framework device object interface for this interrupt object. |
| [IWDFInterrupt::GetInfo](nf-wudfddi-iwdfinterrupt-getinfo.md) | The GetInfo method retrieves information about a specified interrupt. |
| [IWDFInterrupt::QueueWorkItemForIsr](nf-wudfddi-iwdfinterrupt-queueworkitemforisr.md) | The QueueWorkItemForIsr method queues a work item to process interrupt-related work outside of the interrupt service routine. |
| [IWDFInterrupt::ReleaseInterruptLock](nf-wudfddi-iwdfinterrupt-releaseinterruptlock.md) | The ReleaseInterruptLock method ends a code sequence that executes while holding an interrupt object's lock. |
| [IWDFInterrupt::SetExtendedPolicy](nf-wudfddi-iwdfinterrupt-setextendedpolicy.md) | The SetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [IWDFInterrupt::SetPolicy](nf-wudfddi-iwdfinterrupt-setpolicy.md) | The SetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [IWDFInterrupt::TryToAcquireInterruptLock](nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock.md) | The TryToAcquireInterruptLock method acquires the interrupt lock if no other thread has already acquired it. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>