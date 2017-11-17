# Declarations in the printoem header
This header Printoem contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [GETINFO_STDVAR structure](ns-printoem--getinfo-stdvar.md) | The GETINFO_STDVAR structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [DEVOBJ structure](ns-printoem--devobj.md) | TBD |
| [DRVPROCS structure](ns-printoem--drvprocs.md) | TBD |
| [PSCRIPT5_PRIVATE_DEVMODE structure](ns-printoem--pscript5-private-devmode.md) | The PSCRIPT5_PRIVATE_DEVMODE structure enables Pscript5 plug-ins to determine the size of the private portion of Pscript5's DEVMODEW structure. |
| [OEMUIPSPARAM structure](ns-printoem--oemuipsparam.md) | The OEMUIPSPARAM structure is passed to a user interface plug-in's IPrintOemUI |
| [OEM_DMEXTRAHEADER structure](ns-printoem--oem-dmextraheader.md) | The OEM_DMEXTRAHEADER structure must be used to define the first members of a set of private DEVMODEW structure members. |
| [GETINFO_FONTOBJ structure](ns-printoem--getinfo-fontobj.md) | The GETINFO_FONTOBJ structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [OEMCUIPPARAM structure](ns-printoem--oemcuipparam.md) | TBD |
| [PDEV_USE_TRUE_COLOR structure](ns-printoem--pdev-use-true-color.md) | The PDEV_USE_TRUE_COLOR structure indicates whether the output color space should be color or grayscale. |
| [PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure](ns-printoem--pdev-adjust-imageable-origin-area.md) | The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure specifies the imageable origin area. |
| [OEMCUIPPARAM structure](ns-printoem--oemcuipparam~r1.md) | The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI |
| [OEMDMPARAM structure](ns-printoem--oemdmparam.md) | The OEMDMPARAM structure is used as an input parameter to the IPrintOemUI |
| [SIMULATE_CAPS_1 structure](ns-printoem--simulate-caps-1.md) | The SIMULATE_CAPS_1 structure contains information about the types of simulations a spooler supports. |
| [GETINFO_GLYPHSTRING structure](ns-printoem--getinfo-glyphstring.md) | The GETINFO_GLYPHSTRING structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [PIPPARAMS structure](ns-printoem-pipparams.md) | The IPPARAMS structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [PDEV_ADJUST_PHYSICAL_PAPER_SIZE structure](ns-printoem--pdev-adjust-physical-paper-size.md) | TBD |
| [GETINFO_MEMORY structure](ns-printoem--getinfo-memory.md) | The GETINFO_MEMORY structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_GLYPHBITMAP structure](ns-printoem--getinfo-glyphbitmap.md) | The GETINFO_GLYPHBITMAP structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [POEMMEMORYUSAGE structure](ns-printoem-poemmemoryusage.md) | The OEMMEMORYUSAGE structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [PDEV_HOSTFONT_ENABLED structure](ns-printoem--pdev-hostfont-enabled.md) | The PDEV_HOSTFONT_ENABLED structure indicates whether the Hostfont feature is enabled. |
| [UNIDRV_PRIVATE_DEVMODE structure](ns-printoem--unidrv-private-devmode.md) | The UNIDRV_PRIVATE_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure. |
| [PUBLISHERINFO structure](ns-printoem--publisherinfo.md) | The PUBLISHERINFO structure is used as an input parameter to the IPrintOemPS |
| [GETINFO_GLYPHWIDTH structure](ns-printoem--getinfo-glyphwidth.md) | The GETINFO_GLYPHWIDTH structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [USERDATA structure](ns-printoem--userdata.md) | The USERDATA structure is used by Unidrv and Pscript to specify additional information about printer features. A USERDATA structure pointer is supplied as the UserData member for each OPTITEM structure. |
| [OEMUIPROCS structure](ns-printoem--oemuiprocs.md) | The OEMUIPROCS structure is obsolete.The OEMUIPROCS structure contains the address of the DrvGetDriverSetting and DrvUpdateUISetting functions that are exported by Microsoft printer drivers. |
| [PDEV_ADJUST_GRAPHICS_RESOLUTION structure](ns-printoem--pdev-adjust-graphics-resolution.md) | The PDEV_ADJUST_GRAPHICS_RESOLUTION structure specifies a graphics resolution value. |
| [DEVOBJ structure](ns-printoem--devobj~r1.md) | The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods. |
| [PDEV_ADJUST_PAPER_MARGIN structure](ns-printoem--pdev-adjust-paper-margin.md) | The PDEV_ADJUST_PAPER_MARGIN structure specifies the imageable printing area. |
| [FINVOCATION structure](ns-printoem--finvocation.md) | The FINVOCATION structure is used as input to the IPrintOemUni |
| [UNIFONTOBJ structure](ns-printoem--unifontobj.md) | The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins. |
| [CUSTOMSIZEPARAM structure](ns-printoem--customsizeparam.md) | The CUSTOMSIZEPARAM structure holds information pertaining to a single custom page size parameter for a printer. |
| [OEMUIOBJ structure](ns-printoem--oemuiobj.md) | The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [OEMDisableDriver function](nf-printoem-oemdisabledriver.md) | TBD |
| [OEMFillPath function](nf-printoem-oemfillpath.md) | TBD |
| [OEMQueryFontTree function](nf-printoem-oemqueryfonttree.md) | TBD |
| [OEMPrinterEvent function](nf-printoem-oemprinterevent.md) | TBD |
| [OEMStretchBltROP function](nf-printoem-oemstretchbltrop.md) | TBD |
| [OEMEscape function](nf-printoem-oemescape.md) | TBD |
| [OEMGradientFill function](nf-printoem-oemgradientfill.md) | TBD |
| [OEMSendFontCmd function](nf-printoem-oemsendfontcmd.md) | TBD |
| [OEMStartPage function](nf-printoem-oemstartpage.md) | TBD |
| [OEMStartDoc function](nf-printoem-oemstartdoc.md) | TBD |
| [OEMEnablePDEV function](nf-printoem-oemenablepdev.md) | TBD |
| [OEMDevMode function](nf-printoem-oemdevmode.md) | TBD |
| [OEMCommandCallback function](nf-printoem-oemcommandcallback.md) | TBD |
| [OEMTTDownloadMethod function](nf-printoem-oemttdownloadmethod.md) | TBD |
| [OEMFontInstallerDlgProc function](nf-printoem-oemfontinstallerdlgproc.md) | TBD |
| [OEMTransparentBlt function](nf-printoem-oemtransparentblt.md) | TBD |
| [OEMGetGlyphMode function](nf-printoem-oemgetglyphmode.md) | TBD |
| [OEMCommonUIProp function](nf-printoem-oemcommonuiprop.md) | TBD |
| [GET_PSCRIPT5_PRIVATE_DEVMODE_SIZE function](nf-printoem-get-pscript5-private-devmode-size.md) | TBD |
| [OEMTextOut function](nf-printoem-oemtextout.md) | TBD |
| [OEMRealizeBrush function](nf-printoem-oemrealizebrush.md) | TBD |
| [OEMIcmDeleteColorTransform function](nf-printoem-oemicmdeletecolortransform.md) | TBD |
| [OEMResetPDEV function](nf-printoem-oemresetpdev.md) | TBD |
| [OEMPlgBlt function](nf-printoem-oemplgblt.md) | TBD |
| [OEMCopyBits function](nf-printoem-oemcopybits.md) | TBD |
| [OEMDevicePropertySheets function](nf-printoem-oemdevicepropertysheets.md) | TBD |
| [OEMQueryFont function](nf-printoem-oemqueryfont.md) | TBD |
| [GET_UNIDRV_PRIVATE_DEVMODE_SIZE function](nf-printoem-get-unidrv-private-devmode-size.md) | TBD |
| [OEMStrokePath function](nf-printoem-oemstrokepath.md) | TBD |
| [OEMCommand function](nf-printoem-oemcommand.md) | TBD |
| [OEMStrokeAndFillPath function](nf-printoem-oemstrokeandfillpath.md) | TBD |
| [OEMDisablePDEV function](nf-printoem-oemdisablepdev.md) | TBD |
| [OEMPaint function](nf-printoem-oempaint.md) | TBD |
| [OEMDriverDMS function](nf-printoem-oemdriverdms.md) | TBD |
| [OEMHalftonePattern function](nf-printoem-oemhalftonepattern.md) | TBD |
| [OEMQueryAdvanceWidths function](nf-printoem-oemqueryadvancewidths.md) | TBD |
| [OEMDitherColor function](nf-printoem-oemdithercolor.md) | TBD |
| [OEMTextOutAsBitmap function](nf-printoem-oemtextoutasbitmap.md) | TBD |
| [OEMUpgradePrinter function](nf-printoem-oemupgradeprinter.md) | TBD |
| [OEMDeviceCapabilities function](nf-printoem-oemdevicecapabilities.md) | TBD |
| [OEMEnableDriver function](nf-printoem-oemenabledriver.md) | TBD |
| [OEMFilterGraphics function](nf-printoem-oemfiltergraphics.md) | TBD |
| [OEMMemoryUsage function](nf-printoem-oemmemoryusage.md) | TBD |
| [OEMCompression function](nf-printoem-oemcompression.md) | TBD |
| [OEMStretchBlt function](nf-printoem-oemstretchblt.md) | TBD |
| [OEMGetInfo function](nf-printoem-oemgetinfo.md) | TBD |
| [OEMIcmCreateColorTransform function](nf-printoem-oemicmcreatecolortransform.md) | TBD |
| [OEMDevQueryPrintEx function](nf-printoem-oemdevqueryprintex.md) | TBD |
| [OEMQueryColorProfile function](nf-printoem-oemquerycolorprofile.md) | TBD |
| [OEMSendPage function](nf-printoem-oemsendpage.md) | TBD |
| [OEMDocumentPropertySheets function](nf-printoem-oemdocumentpropertysheets.md) | TBD |
| [OEMQueryDeviceSupport function](nf-printoem-oemquerydevicesupport.md) | TBD |
| [OEMUpdateExternalFonts function](nf-printoem-oemupdateexternalfonts.md) | TBD |
| [OEMStartBanding function](nf-printoem-oemstartbanding.md) | TBD |
| [OEMDownloadFontHeader function](nf-printoem-oemdownloadfontheader.md) | TBD |
| [OEMUpgradeRegistry function](nf-printoem-oemupgraderegistry.md) | TBD |
| [OEMEndDoc function](nf-printoem-oemenddoc.md) | TBD |
| [OEMFontManagement function](nf-printoem-oemfontmanagement.md) | TBD |
| [OEMAlphaBlend function](nf-printoem-oemalphablend.md) | TBD |
| [OEMImageProcessing function](nf-printoem-oemimageprocessing.md) | TBD |
| [OEMOutputCharStr function](nf-printoem-oemoutputcharstr.md) | TBD |
| [OEMLineTo function](nf-printoem-oemlineto.md) | TBD |
| [OEMPDriverEvent function](nf-printoem-oempdriverevent.md) | TBD |
| [OEMTTYGetInfo function](nf-printoem-oemttygetinfo.md) | TBD |
| [OEMDownloadCharGlyph function](nf-printoem-oemdownloadcharglyph.md) | TBD |
| [OEMQueryFontData function](nf-printoem-oemqueryfontdata.md) | TBD |
| [OEMBitBlt function](nf-printoem-oembitblt.md) | TBD |
| [OEMNextBand function](nf-printoem-oemnextband.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_DrvGetStandardVariable callback function](nc-printoem-pfn-drvgetstandardvariable.md) | TBD |
| [OEMCUIPCALLBACK callback function](nc-printoem-oemcuipcallback.md) | TBD |
| [PFN_DrvUpgradeRegistrySetting callback function](nc-printoem-pfn-drvupgraderegistrysetting.md) | TBD |
| [PFN_DrvGetDriverSetting callback function](nc-printoem-pfn-drvgetdriversetting.md) | TBD |
| [PFN_DrvUpdateUISetting callback function](nc-printoem-pfn-drvupdateuisetting.md) | TBD |
| [PFN_DrvWriteSpoolBuf callback function](nc-printoem-pfn-drvwritespoolbuf.md) | TBD |
| [PFN_DrvWriteAbortBuf callback function](nc-printoem-pfn-drvwriteabortbuf.md) | TBD |
| [PFN_DrvUnidriverTextOut callback function](nc-printoem-pfn-drvunidrivertextout.md) | TBD |
| [PFN_DrvYMoveTo callback function](nc-printoem-pfn-drvymoveto.md) | TBD |
| [PFNGETINFO callback function](nc-printoem-pfngetinfo.md) | TBD |
| [PFN_DrvXMoveTo callback function](nc-printoem-pfn-drvxmoveto.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [STDVARIABLEINDEX enumeration](ne-printoem--stdvariableindex.md) | TBD. |
| [EATTRIBUTE_DATATYPE enumeration](ne-printoem--eattribute-datatype.md) | The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute. |

This header is used in these topics:

- [print](..content/_print)
