---
UID: NE:pointofservicedriverinterface._PosPropertyId
title: "_PosPropertyId"
author: windows-driver-content
description: This enumeration defines the property identifiers for the properties that device drivers need to handle to be considered a barcode scanner or a magnetic strip reader (MSR).
old-location: pos\pospropertyid.htm
old-project: pos
ms.assetid: 82864db1-ee0a-4d41-a516-4e04befd2e89
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: BarcodeScannerActiveProfile, BarcodeScannerActiveSymbologies, BarcodeScannerCapabilities, BarcodeScannerIsDecodeDataEnabled, BarcodeScannerSupportedProfiles, BarcodeScannerSupportedSymbologies, IsDisabledOnDataReceived, IsEnabled, MagneticStripeReaderCapabilities, MagneticStripeReaderDataEncryptionAlgorithm, MagneticStripeReaderDeviceAuthenticationProtocol, MagneticStripeReaderErrorReportingType, MagneticStripeReaderIsDecodeDataEnabled, MagneticStripeReaderIsDeviceAuthenticated, MagneticStripeReaderIsTransmitSentinelsEnabled, MagneticStripeReaderSupportedCardTypes, MagneticStripeReaderTracksToRead, PosPropertyId, PosPropertyId enumeration, _PosPropertyId, pointofservicedriverinterface/BarcodeScannerActiveProfile, pointofservicedriverinterface/BarcodeScannerActiveSymbologies, pointofservicedriverinterface/BarcodeScannerCapabilities, pointofservicedriverinterface/BarcodeScannerIsDecodeDataEnabled, pointofservicedriverinterface/BarcodeScannerSupportedProfiles, pointofservicedriverinterface/BarcodeScannerSupportedSymbologies, pointofservicedriverinterface/IsDisabledOnDataReceived, pointofservicedriverinterface/IsEnabled, pointofservicedriverinterface/MagneticStripeReaderCapabilities, pointofservicedriverinterface/MagneticStripeReaderDataEncryptionAlgorithm, pointofservicedriverinterface/MagneticStripeReaderDeviceAuthenticationProtocol, pointofservicedriverinterface/MagneticStripeReaderErrorReportingType, pointofservicedriverinterface/MagneticStripeReaderIsDecodeDataEnabled, pointofservicedriverinterface/MagneticStripeReaderIsDeviceAuthenticated, pointofservicedriverinterface/MagneticStripeReaderIsTransmitSentinelsEnabled, pointofservicedriverinterface/MagneticStripeReaderSupportedCardTypes, pointofservicedriverinterface/MagneticStripeReaderTracksToRead, pointofservicedriverinterface/PosPropertyId, pos.pospropertyid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pointofservicedriverinterface.h
req.include-header: Pointofservicedriverinterface.h
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
req.irql: Called at PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pointofservicedriverinterface.h
api_name:
-	PosPropertyId
product: Windows
targetos: Windows
req.typenames: PosPropertyId
---

# _PosPropertyId Enumeration
This enumeration defines the property identifiers for the properties that device drivers need to handle to be considered a barcode scanner or a magnetic strip reader (MSR).

## Syntax
```
typedef enum _PosPropertyId {
  IsEnabled                                         ,
  IsDisabledOnDataReceived                          ,
  PowerState                                        ,
  BarcodeScannerIsDecodeDataEnabled                 ,
  BarcodeScannerCapabilities                        ,
  BarcodeScannerSupportedSymbologies                ,
  BarcodeScannerActiveSymbologies                   ,
  BarcodeScannerSupportedProfiles                   ,
  BarcodeScannerActiveProfile                       ,
  MagneticStripeReaderIsDecodeDataEnabled           ,
  MagneticStripeReaderCapabilities                  ,
  MagneticStripeReaderSupportedCardTypes            ,
  MagneticStripeReaderDeviceAuthenticationProtocol  ,
  MagneticStripeReaderErrorReportingType            ,
  MagneticStripeReaderTracksToRead                  ,
  MagneticStripeReaderIsTransmitSentinelsEnabled    ,
  MagneticStripeReaderIsDeviceAuthenticated         ,
  MagneticStripeReaderDataEncryptionAlgorithm       ,
  BarcodeScannerVideoDeviceId                       ,
  PrinterCapabilities                               ,
  PrinterCartridgeNotifyEnabled                     ,
  PrinterSupportedCharacterSets                     ,
  PrinterFlagWhenIdle                               ,
  PrinterFontTypefaceList                           ,
  PrinterMapCharacterSet                            ,
  PrinterRotateSpecial                              ,
  PrinterSupportedJournalLineChars                  ,
  PrinterSupportedReceiptLineChars                  ,
  PrinterSupportedReceiptBarcodeRotations           ,
  PrinterSupportedReceiptBitmapRotations            ,
  PrinterSupportedSlipLineChars                     ,
  PrinterSupportedSlipBarcodeRotations              ,
  PrinterSupportedSlipBitmapRotations               ,
  PrinterCharacterSet                               ,
  PrinterCoverOpen                                  ,
  PrinterMapMode                                    ,
  PrinterPageModeArea                               ,
  PrinterPageModeDescriptor                         ,
  PrinterPageModeHorizontalPosition                 ,
  PrinterPageModePrintArea                          ,
  PrinterPageModePrintDirection                     ,
  PrinterPageModeStation                            ,
  PrinterPageModeVerticalPosition                   ,
  PrinterJournalLineChars                           ,
  PrinterJournalLineHeight                          ,
  PrinterJournalLineSpacing                         ,
  PrinterJournalLineWidth                           ,
  PrinterJournalLetterQuality                       ,
  PrinterJournalPaperEmpty                          ,
  PrinterJournalPaperNearEnd                        ,
  PrinterJournalCartridgeState                      ,
  PrinterJournalCurrentCartridge                    ,
  PrinterReceiptLineChars                           ,
  PrinterReceiptLineHeight                          ,
  PrinterReceiptLineSpacing                         ,
  PrinterReceiptLineWidth                           ,
  PrinterReceiptLetterQuality                       ,
  PrinterReceiptPaperEmpty                          ,
  PrinterReceiptPaperNearEmpty                      ,
  PrinterReceiptSidewaysMaxLines                    ,
  PrinterReceiptSidewaysMaxChars                    ,
  PrinterReceiptLinesToPaperCut                     ,
  PrinterReceiptCartridgeState                      ,
  PrinterReceiptCurrentCartridge                    ,
  PrinterSlipLineChars                              ,
  PrinterSlipLineHeight                             ,
  PrinterSlipLineSpacing                            ,
  PrinterSlipLineWidth                              ,
  PrinterSlipLetterQuality                          ,
  PrinterSlipPaperEmpty                             ,
  PrinterSlipPaperNearEmpty                         ,
  PrinterSlipSidewaysMaxLines                       ,
  PrinterSlipSideWaysMaxChars                       ,
  PrinterSlipMaxLines                               ,
  PrinterSlipLinesNearEndToEnd                      ,
  PrinterSlipPrintside                              ,
  PrinterSlipCartridgeState                         ,
  PrinterSlipCurrentCartridge                       ,
  PrinterStatusProp                                 ,
  CashDrawerIsDrawerOpened                          ,
  CashDrawerCapabilities                            ,
  CashDrawerStatusProp                              ,
  LineDisplayCapabilities                           ,
  LineDisplayCurrentWindow                          ,
  LineDisplayWindowSizeInCharacters                 ,
  LineDisplayWindowInterCharacterWaitInterval       ,
  LineDisplayPhysicalDeviceName                     ,
  LineDisplayPhysicalDeviceDescription              ,
  LineDisplayDeviceControlDescription               ,
  LineDisplayDeviceControlVersion                   ,
  LineDisplayDeviceServiceVersion                   ,
  LineDisplayCursorTypeProperty                     ,
  LineDisplayCursorAutoUpdateEnabled                ,
  LineDisplayCursorPosition                         ,
  LineDisplayScreenModeList                         ,
  LineDisplayScreenMode                             ,
  LineDisplayMaxBitmapSizeInPixels                  ,
  LineDisplayCharacterSetList                       ,
  LineDisplayDeviceBrightness                       ,
  LineDisplayBlinkRate                              ,
  LineDisplayCharacterSet                           ,
  LineDisplayMapCharacterSet                        ,
  LineDisplayGlyphSizeInPixels                      ,
  LineDisplayCustomGlyphList                        ,
  LineDisplayMarqueeFormat                          ,
  LineDisplayMarqueeRepeatWait                      ,
  LineDisplayMarqueeUnitWait                        ,
  LineDisplayMarqueeType
} PosPropertyId;
```

## Constants

<table>
            
                <tr>
                    <td>IsEnabled</td>
                    <td>Indicates whether the device is enabled. An enabled device is expected to be powered on and fully functional. In a disabled state, the device is not expected to generate input and can be powered down. (Read/Write).</td>
                </tr>
            
                <tr>
                    <td>IsDisabledOnDataReceived</td>
                    <td>Indicates whether to disable the device after each scan event. This allows the hardware to enter an idle power-saving mode as frequently as possible. (Read/Write).</td>
                </tr>
            
                <tr>
                    <td>PowerState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerIsDecodeDataEnabled</td>
                    <td>When set to <b>TRUE</b>, the driver must return decoded bar code data in the form of <b>ScanDataLabel</b> in addition to <b>ScanData</b> when raising a data received event. Decoded barcode data typically only contains data from the scanner with header information, scanner generated symbol character, and length identification removed. (Read/Write).</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerCapabilities</td>
                    <td>Contains information about what functionality the barcode scanner supports. For example, a barcode scanner may support imaging and standard power reporting but not statistics updating and reporting. For more information about the values for barcode capabilities, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn772206">PosBarcodeScannerCapabilitiesType</a>. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerSupportedSymbologies</td>
                    <td>Contains an array representing the complete list of symbologies that the barcode scanner is capable of reading. Also returns the number of bytes required for the array of symbologies. For symbology definitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn757474">BarcodeSymbology</a>. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerActiveSymbologies</td>
                    <td>Indicates the symbologies that the barcode scanner is actively handling. (Write-only). For symbology definitions, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn757474">BarcodeSymbology</a>.</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerSupportedProfiles</td>
                    <td>Returns the list of supported driver-defined device configuration profiles. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerActiveProfile</td>
                    <td>Sets the active device configuration profile. Configure the driver using one of the driver- or manufacturer-defined profiles in the list returned by the <b>BarcodeScannerSupportedProfiles</b> property. (Write-Only). For example, you may have one profile for warehouse staff and another profile for the sales department. Each profile is expected to configure the device based on the driver or manufacturer definition.</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderIsDecodeDataEnabled</td>
                    <td>Indicates whether to provide raw or decoded data from the most recently swiped card. If decoded data is provided to the application, set to <b>true</b>; otherwise, set to <b>false</b>. (Read/write).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderCapabilities</td>
                    <td>Returns a <a href="https://msdn.microsoft.com/library/windows/hardware/dn772235">PosMagneticStripeReaderCapabilitiesType</a> that describes the capabilities of the MSR. (Read-Only).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderSupportedCardTypes</td>
                    <td>Returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/dn772167">MsrCardType</a>s supported by the MSR. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderDeviceAuthenticationProtocol</td>
                    <td>The driver must return a <a href="https://msdn.microsoft.com/6f06d03e-001e-4340-9b96-8e3654be5c1a">MsrAuthenticationProtocolType</a> that describes the device authentication protocol supported by the MSR. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderErrorReportingType</td>
                    <td>Specifies the level of error reporting that the MSR supports. For more information about the values for error reporting levels, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn772170">MsrErrorReportingType</a>. (Read/write).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderTracksToRead</td>
                    <td>Specifies which tracks the application will receive following a card swipe. Does not indicate the capability of the device hardware; instead, it is an application-configurable property representing the tracks to be read. For more information about track values, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn772176">MsrTrackIds</a>. (Read/write).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderIsTransmitSentinelsEnabled</td>
                    <td>Indicates whether the track data contains start and end sentinel values. (Read/write).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderIsDeviceAuthenticated</td>
                    <td>Indicates whether the device is authenticated. (Read-only).</td>
                </tr>
            
                <tr>
                    <td>MagneticStripeReaderDataEncryptionAlgorithm</td>
                    <td>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/dn772169">MsrDataEncryption</a> that will be used to encrypt the track data. (Read/write).</td>
                </tr>
            
                <tr>
                    <td>BarcodeScannerVideoDeviceId</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterCapabilities</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterCartridgeNotifyEnabled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedCharacterSets</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterFlagWhenIdle</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterFontTypefaceList</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterMapCharacterSet</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterRotateSpecial</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedJournalLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedReceiptLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedReceiptBarcodeRotations</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedReceiptBitmapRotations</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedSlipLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedSlipBarcodeRotations</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSupportedSlipBitmapRotations</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterCharacterSet</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterCoverOpen</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterMapMode</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModeArea</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModeDescriptor</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModeHorizontalPosition</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModePrintArea</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModePrintDirection</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModeStation</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterPageModeVerticalPosition</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalLineHeight</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalLineSpacing</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalLineWidth</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalLetterQuality</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalPaperEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalPaperNearEnd</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalCartridgeState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterJournalCurrentCartridge</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLineHeight</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLineSpacing</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLineWidth</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLetterQuality</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptPaperEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptPaperNearEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptSidewaysMaxLines</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptSidewaysMaxChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptLinesToPaperCut</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptCartridgeState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterReceiptCurrentCartridge</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLineChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLineHeight</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLineSpacing</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLineWidth</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLetterQuality</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipPaperEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipPaperNearEmpty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipSidewaysMaxLines</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipSideWaysMaxChars</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipMaxLines</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipLinesNearEndToEnd</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipPrintside</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipCartridgeState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterSlipCurrentCartridge</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>PrinterStatusProp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>CashDrawerIsDrawerOpened</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>CashDrawerCapabilities</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>CashDrawerStatusProp</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCapabilities</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCurrentWindow</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayWindowSizeInCharacters</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayWindowInterCharacterWaitInterval</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayPhysicalDeviceName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayPhysicalDeviceDescription</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayDeviceControlDescription</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayDeviceControlVersion</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayDeviceServiceVersion</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCursorTypeProperty</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCursorAutoUpdateEnabled</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCursorPosition</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayScreenModeList</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayScreenMode</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMaxBitmapSizeInPixels</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCharacterSetList</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayDeviceBrightness</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayBlinkRate</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCharacterSet</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMapCharacterSet</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayGlyphSizeInPixels</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayCustomGlyphList</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMarqueeFormat</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMarqueeRepeatWait</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMarqueeUnitWait</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>LineDisplayMarqueeType</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn772098">IOCTL_POINT_OF_SERVICE_GET_PROPERTY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn772123">IOCTL_POINT_OF_SERVICE_SET_PROPERTY</a>