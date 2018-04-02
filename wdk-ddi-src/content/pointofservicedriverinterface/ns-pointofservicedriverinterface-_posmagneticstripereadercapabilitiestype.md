---
UID: NS:pointofservicedriverinterface._PosMagneticStripeReaderCapabilitiesType
title: "_PosMagneticStripeReaderCapabilitiesType"
author: windows-driver-content
description: This structure defines the kinds of magnetic stripe reader (MSR) capabilities that a device supports, such as whether the device supports track data masking.
old-location: pos\posmagneticstripereadercapabilitiestype.htm
old-project: pos
ms.assetid: 8f5ad241-a145-468d-bd69-7956985152b5
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: PosMagneticStripeReaderCapabilitiesType, PosMagneticStripeReaderCapabilitiesType structure, _PosMagneticStripeReaderCapabilitiesType, pointofservicedriverinterface/PosMagneticStripeReaderCapabilitiesType, pos.posmagneticstripereadercapabilitiestype
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pointofservicedriverinterface.h
req.include-header: PointOfServiceDriverInterface.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	PointOfServiceDriverInterface.h
api_name:
-	PosMagneticStripeReaderCapabilitiesType
product:
- Windows
targetos: Windows
req.typenames: PosMagneticStripeReaderCapabilitiesType
---

# _PosMagneticStripeReaderCapabilitiesType structure
This structure defines the kinds of magnetic stripe reader (MSR) capabilities that a device supports, such as whether the device supports track data masking.

## Syntax
```
typedef struct _PosMagneticStripeReaderCapabilitiesType {
  DriverUnifiedPosPowerReportingType            PowerReportingType;
  LONG                                          IsStatisticsReportingSupported;
  LONG                                          IsStatisticsUpdatingSupported;
  UINT32                                        CardAuthenticationLength;
  UINT32                                        SupportedEncryptionAlgorithms;
  DriverMagneticStripeReaderAuthenticationLevel AuthenticationLevel;
  LONG                                          IsIsoSupported;
  LONG                                          IsJisOneSupported;
  LONG                                          IsJisTwoSupported;
  LONG                                          IsTrackDataMaskingSupported;
  LONG                                          IsTransmitSentinelsSupported;
} PosMagneticStripeReaderCapabilitiesType;
```

## Members


`PowerReportingType`

Indicates the type of power reporting that is supported by the device.

`IsStatisticsReportingSupported`

Indicates whether the device supports <a href="https://msdn.microsoft.com/library/windows/hardware/dn772120">IOCTL_POINT_OF_SERVICE_RETRIEVE_STATISTICS</a>.

`IsStatisticsUpdatingSupported`

Indicates whether the device supports <a href="https://msdn.microsoft.com/library/windows/hardware/dn772126">IOCTL_POINT_OF_SERVICE_UPDATE_STATISTICS</a>.

`CardAuthenticationLength`

The length, in bytes, of the name of the type of authentication that the device uses.

`SupportedEncryptionAlgorithms`

The supported encryption algorithm. See <a href="https://msdn.microsoft.com/library/windows/hardware/dn772169">MsrDataEncryption</a>.

`AuthenticationLevel`

The authentication level that the device supports.

`IsIsoSupported`

Indicates whether the device supports ISO cards.

`IsJisOneSupported`

Indicates whether device supports JIS Type-I cards.

`IsJisTwoSupported`

Indicates whether device supports JIS Type-II cards.

`IsTrackDataMaskingSupported`

Indicates whether the device is capable of masking track data.

`IsTransmitSentinelsSupported`

Indicates whether the devices is able to transmit start and end sentinels.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include PointOfServiceDriverInterface.h) |