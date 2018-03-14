---
UID: NA:wdtf
ms.assetid: 14e419d2-ee55-3451-99ed-6d9c21181fb2
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Wdtf.h header



This header is used by dtf. For more information, see
- [dtf](../_dtf/index.md)

Wdtf.h contain these programming interfaces:


## Enumerations

| Title   | Description   |
| ---- |:---- |
| [__MIDL___MIDL_itf_wdtf_0000_0001_0001 enumeration](ne-wdtf-__midl___midl_itf_wdtf_0000_0001_0001.md) | The TTraceLevel enumeration defines a set of levels for tracing in WDTF. The meaning on each level depends on registry settings for the ITracer interface. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IAction interface](nn-wdtf-iaction.md) | The IAction interfaces are plug-ins that can control an instance of the IWDTFTarget2 interface. |
| [ITracer interface](nn-wdtf-itracer.md) | The ITracer interface enables individual instances of every WDTF interface to determine the specific tracing settings for a given implementation coclass. These settings are recorded in the registry. |
| [ITracing interface](nn-wdtf-itracing.md) | The ITracing interface sets an object's TTraceLevel value. This interface is a base interface for most of the WDTF interfaces. |
| [IWDTF2 interface](nn-wdtf-iwdtf2.md) | Defines properties for the WDTF collection. |
| [IWDTFAction2 interface](nn-wdtf-iwdtfaction2.md) | Defines operations and properties that can control an instance of the IWDTFTarget2 interface. |
| [IWDTFActions2 interface](nn-wdtf-iwdtfactions2.md) | Defines operations and properties for the collection of actions that the IWDTFTargets |
| [IWDTFCONFIG2 interface](nn-wdtf-iwdtfconfig2.md) | Defines operations that control WDTF objects within a test script. |
| [IWDTFDeviceDepot2 interface](nn-wdtf-iwdtfdevicedepot2.md) | Defines properties and operations for the collection of devices on a computer. |
| [IWDTFLOG2 interface](nn-wdtf-iwdtflog2.md) | Defines operations that enable the test case author to add to the WDTF test log. |
| [IWDTFLongNumbers2 interface](nn-wdtf-iwdtflongnumbers2.md) | Defines operations and properties for a collection of long numbers. |
| [IWDTFNumbers2 interface](nn-wdtf-iwdtfnumbers2.md) | Defines operations and properties for a collection of numbers. |
| [IWDTFStrings2 interface](nn-wdtf-iwdtfstrings2.md) | Defines operations and properties for a collection of strings. |
| [IWDTFSystemDepot2 interface](nn-wdtf-iwdtfsystemdepot2.md) | Defines operations and properties for the SystemDepot - the object that represents the local computer. |
| [IWDTFTarget2 interface](nn-wdtf-iwdtftarget2.md) | Defines operations and properties for a testable item. |
| [IWDTFTargets2 interface](nn-wdtf-iwdtftargets2.md) | Defines properties and operations for the collection. |

## Methods

| Title   | Description   |
| ---- |:----

# wdtf.h header



wdtf.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IAction](nn-wdtf-iaction.md) | The IAction interfaces are plug-ins that can control an instance of the IWDTFTarget2 interface. |
| [ITracer](nn-wdtf-itracer.md) | The ITracer interface enables individual instances of every WDTF interface to determine the specific tracing settings for a given implementation coclass. These settings are recorded in the registry. |
| [ITracing](nn-wdtf-itracing.md) | The ITracing interface sets an object's TTraceLevel value. This interface is a base interface for most of the WDTF interfaces. |
| [IWDTF2](nn-wdtf-iwdtf2.md) | Defines properties for the WDTF collection. |
| [IWDTFAction2](nn-wdtf-iwdtfaction2.md) | Defines operations and properties that can control an instance of the IWDTFTarget2 interface. |
| [IWDTFActions2](nn-wdtf-iwdtfactions2.md) | Defines operations and properties for the collection of actions that the IWDTFTargets::GetInterfaces method returns. |
| [IWDTFCONFIG2](nn-wdtf-iwdtfconfig2.md) | Defines operations that control WDTF objects within a test script. |
| [IWDTFDeviceDepot2](nn-wdtf-iwdtfdevicedepot2.md) | Defines properties and operations for the collection of devices on a computer. |
| [IWDTFLOG2](nn-wdtf-iwdtflog2.md) | Defines operations that enable the test case author to add to the WDTF test log. |
| [IWDTFLongNumbers2](nn-wdtf-iwdtflongnumbers2.md) | Defines operations and properties for a collection of long numbers. |
| [IWDTFNumbers2](nn-wdtf-iwdtfnumbers2.md) | Defines operations and properties for a collection of numbers. |
| [IWDTFStrings2](nn-wdtf-iwdtfstrings2.md) | Defines operations and properties for a collection of strings. |
| [IWDTFSystemDepot2](nn-wdtf-iwdtfsystemdepot2.md) | Defines operations and properties for the SystemDepot - the object that represents the local computer. |
| [IWDTFTarget2](nn-wdtf-iwdtftarget2.md) | Defines operations and properties for a testable item. |
| [IWDTFTargets2](nn-wdtf-iwdtftargets2.md) | Defines properties and operations for the collection. |






## Enumerations
| Title | Description |
| ---- |:---- |
| [__MIDL___MIDL_itf_wdtf_0000_0001_0001](ne-wdtf-__midl___midl_itf_wdtf_0000_0001_0001.md) | The TTraceLevel enumeration defines a set of levels for tracing in WDTF. The meaning on each level depends on registry settings for the ITracer interface. |