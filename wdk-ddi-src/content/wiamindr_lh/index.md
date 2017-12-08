# Wiamindr_Lh.h header


This header is used by Imaging devices. For more information, see
- [Imaging devices](../_image/index.md)

Wiamindr_Lh.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [IWiaDrvItem::AddItemToFolder method](nf-wiamindr-lh-iwiadrvitem-additemtofolder.md) | The IWiaDrvItem |
| [IWiaDrvItem::DumpItemData method](nf-wiamindr-lh-iwiadrvitem-dumpitemdata.md) | The IWiaDrvItem |
| [IWiaDrvItem::FindChildItemByName method](nf-wiamindr-lh-iwiadrvitem-findchilditembyname.md) | The IWiaDrvItem |
| [IWiaDrvItem::FindItemByName method](nf-wiamindr-lh-iwiadrvitem-finditembyname.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetDeviceSpecContext method](nf-wiamindr-lh-iwiadrvitem-getdevicespeccontext.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetFirstChildItem method](nf-wiamindr-lh-iwiadrvitem-getfirstchilditem.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetFullItemName method](nf-wiamindr-lh-iwiadrvitem-getfullitemname.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetItemFlags method](nf-wiamindr-lh-iwiadrvitem-getitemflags.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetItemName method](nf-wiamindr-lh-iwiadrvitem-getitemname.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetNextSiblingItem method](nf-wiamindr-lh-iwiadrvitem-getnextsiblingitem.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetParentItem method](nf-wiamindr-lh-iwiadrvitem-getparentitem.md) | The IWiaDrvItem |
| [IWiaDrvItem::RemoveItemFromFolder method](nf-wiamindr-lh-iwiadrvitem-removeitemfromfolder.md) | The IWiaDrvItem |
| [IWiaDrvItem::UnlinkItemTree method](nf-wiamindr-lh-iwiadrvitem-unlinkitemtree.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvAcquireItemData method](nf-wiamindr-lh-iwiaminidrv-drvacquireitemdata.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvAnalyzeItem method](nf-wiamindr-lh-iwiaminidrv-drvanalyzeitem.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvDeleteItem method](nf-wiamindr-lh-iwiaminidrv-drvdeleteitem.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvDeviceCommand method](nf-wiamindr-lh-iwiaminidrv-drvdevicecommand.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvFreeDrvItemContext method](nf-wiamindr-lh-iwiaminidrv-drvfreedrvitemcontext.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvGetCapabilities method](nf-wiamindr-lh-iwiaminidrv-drvgetcapabilities.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvGetDeviceErrorStr method](nf-wiamindr-lh-iwiaminidrv-drvgetdeviceerrorstr.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvGetWiaFormatInfo method](nf-wiamindr-lh-iwiaminidrv-drvgetwiaformatinfo.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvInitItemProperties method](nf-wiamindr-lh-iwiaminidrv-drvinititemproperties.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvInitializeWia method](nf-wiamindr-lh-iwiaminidrv-drvinitializewia.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvLockWiaDevice method](nf-wiamindr-lh-iwiaminidrv-drvlockwiadevice.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvNotifyPnpEvent method](nf-wiamindr-lh-iwiaminidrv-drvnotifypnpevent.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvReadItemProperties method](nf-wiamindr-lh-iwiaminidrv-drvreaditemproperties.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvUnInitializeWia method](nf-wiamindr-lh-iwiaminidrv-drvuninitializewia.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvUnLockWiaDevice method](nf-wiamindr-lh-iwiaminidrv-drvunlockwiadevice.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvValidateItemProperties method](nf-wiamindr-lh-iwiaminidrv-drvvalidateitemproperties.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvWriteItemProperties method](nf-wiamindr-lh-iwiaminidrv-drvwriteitemproperties.md) | The IWiaMiniDrv |
| [IWiaMiniDrvCallBack::MiniDrvCallback method](nf-wiamindr-lh-iwiaminidrvcallback-minidrvcallback.md) | The IWiaMiniDrvCallBack |
| [IWiaMiniDrvTransferCallback::GetNextStream method](nf-wiamindr-lh-iwiaminidrvtransfercallback-getnextstream.md) | Called by the WIA mini-driver to obtain a stream for the current data transfer (download or upload). |
| [IWiaMiniDrvTransferCallback::SendMessage method](nf-wiamindr-lh-iwiaminidrvtransfercallback-sendmessage.md) | Periodically called by the WIA mini-driver during a data transfer, to update the WIA application client about the progress and status of the transfer. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [MINIDRV_TRANSFER_CONTEXT structure](ns-wiamindr-lh--minidrv-transfer-context.md) | The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer. |
| [MINIDRV_TRANSFER_CONTEXT structure](ns-wiamindr-lh--minidrv-transfer-context~r1.md) | The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer. |
| [WIAS_CHANGED_VALUE_INFO structure](ns-wiamindr-lh--wias-changed-value-info.md) | The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property. |
| [WIAS_CHANGED_VALUE_INFO structure](ns-wiamindr-lh--wias-changed-value-info~r1.md) | The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property. |
| [WIAS_DOWN_SAMPLE_INFO structure](ns-wiamindr-lh--wias-down-sample-info.md) | The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer. |
| [WIAS_DOWN_SAMPLE_INFO structure](ns-wiamindr-lh--wias-down-sample-info~r1.md) | The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer. |
| [WIAS_ENDORSER_INFO structure](ns-wiamindr-lh--wias-endorser-info.md) | The WIAS_ENDORSER_INFO structure holds custom endorser token/value pairs. |
| [WIAS_ENDORSER_INFO structure](ns-wiamindr-lh--wias-endorser-info~r1.md) | The WIAS_ENDORSER_INFO structure holds custom endorser token/value pairs. |
| [WIAS_ENDORSER_VALUE structure](ns-wiamindr-lh--wias-endorser-value.md) | The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings. |
| [WIAS_ENDORSER_VALUE structure](ns-wiamindr-lh--wias-endorser-value~r1.md) | The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings. |
| [WIA_DEV_CAP_DRV structure](ns-wiamindr-lh--wia-dev-cap-drv.md) | The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports. |
| [WIA_DEV_CAP_DRV structure](ns-wiamindr-lh--wia-dev-cap-drv~r1.md) | The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports. |
| [WIA_PROPERTY_CONTEXT structure](ns-wiamindr-lh--wia-property-context.md) | The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. |
| [WIA_PROPERTY_CONTEXT structure](ns-wiamindr-lh--wia-property-context~r1.md) | The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. |
| [WIA_PROPERTY_INFO structure](ns-wiamindr-lh--wia-property-info.md) | The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type. |
| [WIA_PROPERTY_INFO structure](ns-wiamindr-lh--wia-property-info~r1.md) | The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IWiaMiniDrvTransferCallback interface](nn-wiamindr-lh-iwiaminidrvtransfercallback.md) | This is a Callback interface that is called by the WIA mini-driver for stream-based transfers. |
| [IWiaMiniDrvTransferCallback interface](nn-wiamindr-lh-iwiaminidrvtransfercallback~r1.md) | This is a Callback interface that is called by the WIA mini-driver for stream-based transfers. |
